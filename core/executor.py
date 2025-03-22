import importlib
import logging

class Executor:
    def __init__(self, mode, config):
        self.mode = mode
        self.config = config

    def execute(self, module_name):
        try:
            module_path = f"modules.{module_name}.{module_name}_module"
            module = importlib.import_module(module_path)
            module.run(self.mode, self.config)
        except Exception as e:
            logging.error(f"Error executing {module_name}: {e}")