from .logger_impl import LoggerImpl


import requests
import json

import urllib.parse

class TelegramLogger(LoggerImpl):

    def __init__(self, token, chat_id, config: dict = None):
        if config is None:
            config = {}

        if "headers" not in config:
            config["headers"] = {'Content-Type': 'application/x-www-form-urlencoded'}
       
        self.url = f"https://api.telegram.org/bot{token}/sendMessage?"
        self.chat_id = chat_id

        self.config = config

    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        url = self.url

        headers = self.config["headers"]

        mergedPostFields = {
            "chat_id": self.chat_id,
            "text": json.dumps(message, indent=4)
        }
            
        url += urllib.parse.urlencode(mergedPostFields)
        
        return requests.get(url=url, headers=headers, timeout=10)