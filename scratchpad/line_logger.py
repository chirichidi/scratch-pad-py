from .logger_impl import LoggerImpl


import requests
import json

class LineLogger(LoggerImpl):

    def __init__(self, token, config: dict = None):
        if config is None:
            config = {}
        if "url" not in config:
            config["url"] = "https://notify-api.line.me/api/notify"

        if "headers" not in config:
            config["headers"] = {}
        config["headers"].update({'Authorization': 'Bearer ' + token})        

        self.config = config

    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        url = self.config["url"]
        headers = self.config["headers"]

        mergedPostFields = {
            "message": json.dumps(message, indent=4)
        }

        return requests.post(url=url, headers=headers, data=mergedPostFields)