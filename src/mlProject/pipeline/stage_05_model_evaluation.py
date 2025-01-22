from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger


STAGE_NAME = "Model Evaluation"

class ModelEvaluation_Training_Pipeline:
    def __init__(self):
        self.logger = logger


    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.save_results()
        except Exception as e:
            raise e
        


