from mlProject.components.data_transformation import DataTransformation 
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation"


class DataTransformation_Training_Pipeline:
    def __init__(self):
        self.logger = logger

    def main(self):
        try:

            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                status = file.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            
            else:
                raise Exception("Your data schema is not valid. Please validate your data schema first.")
            

        except Exception as e:
            raise e


