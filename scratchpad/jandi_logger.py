from .logger_impl import LoggerImpl


import requests
import json

class JandiLogger(LoggerImpl):

    def __init__(self, url, config: dict = {}):

        self.url = url
        if "headers" not in config:
            config["headers"] = {}        
       
        self.config = config

    def log(self, message: dict, option: dict = {}):

        url = self.url

        headers = self.config["headers"]

        mergedPostFields = {
            "body": json.dumps(message, indent=4)
        }

        return requests.post(url=url, headers=headers, data=mergedPostFields)