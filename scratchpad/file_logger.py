from .logger_impl import LoggerImpl

import json

class FileLogger(LoggerImpl):

    def __init__(self, config: dict = None):
        if config is None:
            config = {}

        if "truncate" not in config:
            config["truncate"] = False
        
        if config["truncate"] == True:
            with open(config["filePath"], "w") as file:
                file.truncate()

        self.config = config

    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        with open(self.config["filePath"], 'a') as file:
            file.write(json.dumps(message) + "\n")