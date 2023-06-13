from .logger_impl import LoggerImpl

import json
import requests

class SlackLogger(LoggerImpl):
    
    
    
    def __init__(self, url, config: dict = None) -> None:
        if config is None:
            config = {}
            
        if "url" not in config:
            config["url"] = url

        self.config = config
            
        
    def log(self, message: dict, option: dict = None):
        """"
        https://api.slack.com/messaging/webhooks
        """
        headers = {
            "Content-type": "application/json"
        }
        mergedPostFields = json.dumps({
            "text": json.dumps(message, indent=4)
        }, indent=4)
        url = self.config["url"]
        
        return requests.post(url=url, headers=headers, data=mergedPostFields)