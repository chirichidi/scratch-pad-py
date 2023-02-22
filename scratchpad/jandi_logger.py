from .logger_impl import LoggerImpl


import requests
import json

class JandiLogger(LoggerImpl):

    def __init__(self, url, config: dict = None):
        if config is None:
            config = {}

        self.url = url
        if "headers" not in config:
            config["headers"] = {}
        if "body" not in config:
            config["body"] = {}
       
        self.config = config

    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        url = self.url
        headers = self.config["headers"]

        is_with_style = "connectColor" in option and "connectInfo" in option
        if is_with_style == True:
            mergedPostFields = {
                "body": ', '.join("{!s}={!r}".format(key,val) for (key,val) in message.items()),
                "connectColor": option["connectColor"],
                "connectInfo": option["connectInfo"] 
            }
            mergedPostFields = json.dumps(mergedPostFields, indent=4)
        else:
            mergedPostFields = {
                "body": json.dumps(message, indent=4)
            }

        return requests.post(url=url, headers=headers, data=mergedPostFields, timeout=5)