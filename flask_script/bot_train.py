from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_core.agent import *
from rasa_core.policies import *
import os


def train_qa_nlu(path_prefix, slash, time_str):
    core_model_directory=path_prefix+"now_models"+slash+"core"
    nlu_directory_path=path_prefix+"now_models"+slash+"nlu"
    qa_model_directory=nlu_directory_path+slash+"qa"
    task_model_directory=nlu_directory_path+slash+"task"

    training_data = load_data(path_prefix + 'training' + slash + 'd.json')
    trainer = Trainer(config.load(path_prefix + "nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist(path=path_prefix + 'old_models' + slash + 'nlu', project_name='qa',
                                      fixed_model_name='qa' + "_" + time_str)  # Returns the directory the model is stored in

    return model_directory


def train_task_nlu(path_prefix, slash, time_str):
    training_data = load_data(path_prefix + 'training' + slash + 'd.json')
    trainer = Trainer(config.load(path_prefix + "nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist(path=path_prefix + 'old_models' + slash + 'nlu', project_name='task',
                                      fixed_model_name='task' + "_" + time_str)  # Returns the directory the model is stored in
    return model_directory


def train_core(path_prefix, slash, time_str):
    domain_file = path_prefix + "training" + slash + "domain.yml"
    model_path = path_prefix + "old_models" + slash + "core" + slash + "core" + "_" + time_str
    training_data_file = path_prefix + "training" + slash + "story.md"

    fallback = FallbackPolicy(fallback_action_name="utter_default",
                              core_threshold=0.6,
                              nlu_threshold=0.6)
    agent = Agent(domain_file, policies=[KerasPolicy(), fallback])
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)
    return model_path


if __name__ == "__main__":
    train_qa_nlu()
    train_task_nlu()
    train_core()
