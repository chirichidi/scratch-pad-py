from .logger_impl import LoggerImpl

import json
import requests

class SlackLogger(LoggerImpl):
    
    
    
    def __init__(self, url, channel: str = None, config: dict = None) -> None:
        if config is None:
            config = {}
            
        if "url" not in config:
            config["url"] = url

        if channel is not None:
            config["channel"] = channel

        self.config = config
            
        
    def log(self, message: dict, option: dict = None):
        """"
        https://api.slack.com/messaging/webhooks
        """
        headers = {
            "Content-type": "application/json"
        }

        postFields = {
            "text": json.dumps(message, indent=4)
        }

        channel = self.config.get("channel")
        if channel is not None:
            postFields["channel"] = channel

        mergedPostFields = json.dumps(postFields)
        url = self.config["url"]
        
        return requests.post(url=url, headers=headers, data=mergedPostFields)