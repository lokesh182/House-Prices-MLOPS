import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
'''
Generate the file structure
'''

project_name = "HousePricing"

list_of_files = [
    "steps/data_ingest.py",
    "steps/data_splitter.py",
    "steps/process_data.py",
    "steps/deployer.py",
    "steps/evaluator.py",
    "steps/refine_model.py",
    "steps/predict_step.py",
    "steps/train_model.py",
    "steps/predict_service_loader_step.py",
    "steps/deployment_trigger.py",
    "pipelines/continous_deployment_pipeline.py",
    "pipelines/inference_pipeline.py",
    "pipelines/training_pipeline.py",
    "Dockerfile",
    "requirements.txt",
    "run_pipeline.py",
    "run_cid_pipeline.py",
    "constants.py",
    "data/empty.csv",
    "config/train_pipeline.yaml",
    "materializer/custom_materializer.py",
    "notebooks/eda.py"
  
    
    


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")

