from .logger_impl import LoggerImpl

import json

class ConsoleLogger(LoggerImpl):

    def __init__(self, config: dict = None):
        if config is None:
            config = {}
        self.config = config

    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}
            
        appendNewLine = 0
        if "appendNewLine" in self.config:
            appendNewLine = self.config["appendNewLine"]
        if "appendNewLine" in option:
            appendNewLine = option["appendNewLine"]

        print(json.dumps(message))
        if appendNewLine > 0:
            print("\n" * appendNewLine)