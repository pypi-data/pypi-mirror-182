import importlib.util
from nova_server.utils.thread_utils import THREADS
from nova_server.utils.status_utils import update_progress
from nova_server.utils.key_utils import get_key_from_request_form
from nova_server.utils import status_utils, thread_utils, log_utils, dataset_utils, db_utils
from nova_server.utils import polygon_utils
import numpy as np
import os
from pathlib import Path
import nova_server.utils.path_config as cfg
from flask import Blueprint, request, jsonify
from nova_server.utils import thread_utils, status_utils, log_utils, dataset_utils
from nova_server.utils.ssi_utils import Trainer


predict = Blueprint("predict", __name__)


@predict.route("/predict", methods=["POST"])
def predict_thread():
    if request.method == "POST":
        request_form = request.form.to_dict()
        key = get_key_from_request_form(request_form)
        thread = predict_data(request_form)
        status_utils.add_new_job(key)
        data = {"success": "true"}
        thread.start()
        THREADS[key] = thread
        return jsonify(data)


@thread_utils.ml_thread_wrapper
def predict_data(request_form):
    key = get_key_from_request_form(request_form)
    logger = log_utils.get_logger_for_thread(key)

    try:
        logger.info("Action 'Predict' started.")
        status_utils.update_status(key, status_utils.JobStatus.RUNNING)
        sessions = request_form["sessions"].split(";")
        trainer_file_path = Path(cfg.cml_dir + request_form["trainerFilePath"])
        trainer = Trainer()

        if not trainer_file_path.is_file():
            logger.error("Trainer file not available!")
            status_utils.update_status(key, status_utils.JobStatus.ERROR)
            return None
        else:
            trainer.load_from_file(trainer_file_path)
            logger.info("Trainer successfully loaded.")

        if not trainer.model_script_path:
            logger.error('Trainer has no attribute "script" in model tag.')
            status_utils.update_status(key, status_utils.JobStatus.ERROR)
            return None

        # Load Trainer
        model_script_path = trainer_file_path.parent / trainer.model_script_path
        spec = importlib.util.spec_from_file_location("model_script", model_script_path)
        model_script = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(model_script)

        # Set Options 
        logger.info("Setting options...")
        if not request_form["OptStr"] == '':
            for k, v in dict(option.split("=") for option in request_form["OptStr"].split(";")).items():
            model_script.OPTIONS[k] = v
            logger.info('...Option: ' + k + '=' + v)
        logger.info("...done.")

        # Load Model
        model_weight_path = trainer_file_path.parent / trainer.model_weights_path
        logger.info("Loading model...")
        model = model_script.load(model_weight_path, trainer.classes, logger=logger)
        logger.info("...done")


        # Load Data
        for session in sessions:
            request_form["sessions"] = session # overwrite so we handle each session seperatly..
            try:
                update_progress(key, 'Data loading')
                ds_iter = dataset_utils.dataset_from_request_form(request_form)
                logger.info("Prediction data successfully loaded.")
            except ValueError:
                log_utils.remove_log_from_dict(key)
                logger.error("Not able to load the data from the database!")
                status_utils.update_status(key, status_utils.JobStatus.ERROR)
                return

            if request_form["schemeType"] == "DISCRETE_POLYGON" or request_form["schemeType"] == "POLYGON":
                logger.info("Preprocessing data...")
                data_list, labels = model_script.preprocess(ds_iter, logger=logger)
                output_shape = np.uint8(data_list[0][list(data_list[0])[1]])[0].shape
                logger.info("...done")

                logger.info("Predicting results...")
                confidences_layer = model_script.predict(model, data_list, output_shape, logger=logger)
                logger.info("...done")

                logger.info("Postprocessing results...")
                # 2. Create True/False Bitmaps
                binary_masks = polygon_utils.prediction_to_binary_mask(confidences_layer)
                # 3. Get Polygons
                all_polygons = polygon_utils.mask_to_polygons(binary_masks)
                # 4. Get Confidences
                confidences = polygon_utils.get_confidences_from_predictions(confidences_layer, all_polygons)
                logger.info("...done")
                logger.info("Writing data to database...")
                # 5. Write to database
                db_utils.write_polygons_to_db(request_form, all_polygons, confidences, logger)
                logger.info("...done")
            else:
                # 2. Preprocess data
                logger.info("Preprocessing data...")
                ds_iter_pp = model_script.preprocess(ds_iter, logger=logger, request_form=request_form)
                logger.info("...done")

                # 3. Predict data
                logger.info("Predicting results...")
                results = model_script.predict(model, ds_iter_pp, logger=logger)
                logger.info("...done")

                # 5. Write to database
                logger.info("Uploading to database...")
                db_utils.write_annotation_to_db(request_form, results)
                logger.info("...done")

            # 5. In CML case, delete temporary files..
            if request_form["deleteFiles"] == "True":
                logger.info('Deleting temporary CML files...')
                out_dir = Path(cfg.cml_dir + request_form["trainerOutputDirectory"])
                trainer_name = request_form["trainerName"]
                os.remove(out_dir / trainer.model_weights_path)
                os.remove(out_dir / trainer.model_script_path)
                for f in model_script.DEPENDENCIES:
                    os.remove(trainer_file_path.parent / f)
                trainer_fullname = trainer_name + ".trainer"
                os.remove(out_dir / trainer_fullname)
                logger.info('...done')

        logger.info('Prediction completed!')
        status_utils.update_status(key, status_utils.JobStatus.FINISHED)

    except Exception as e:
        logger.error('Error:' + str(e))
        status_utils.update_status(key, status_utils.JobStatus.ERROR)
