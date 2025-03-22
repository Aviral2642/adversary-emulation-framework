import yaml
from core.executor import Executor
import logging

class Scheduler:
    def __init__(self, playbook_path, mode, config):
        self.playbook_path = playbook_path
        self.mode = mode
        self.executor = Executor(mode, config)

    def run(self):
        with open(self.playbook_path, "r") as f:
            playbook = yaml.safe_load(f)

        logging.info(f"Running playbook: {playbook['name']} in mode: {self.mode}")
        for step in playbook["steps"]:
            tactic = step["tactic"]
            technique_id = step["technique_id"]
            module_name = step["module"]
            logging.info(f"--> {tactic} | {technique_id} | {module_name}")
            self.executor.execute(module_name)