from .logger_impl import LoggerImpl
from .logger_interface import LoggerInterface

class CompositeLogger(LoggerImpl):
    def __init__(self, config = {}):
        if "loggerFilterPairs" not in config:
            config["loggerFilterPairs"] = []
        if "defaults" not in config:
            config["defaults"] = {}

        self.config = config


    def log(self, message: dict, option: dict = {}):
        mergedMessage = {}
        if len(self.config["defaults"]) > 0:
            mergedMessage: dict = self.config["defaults"]
            for k, v in mergedMessage.items():
                if callable(v):
                    v()
        
        mergedMessage.update(message)

        for loggerFilterParis in self.config["loggerFilterPairs"]:
            logger: LoggerInterface = loggerFilterParis["logger"]
            filter_ = loggerFilterParis["filter"]

            if filter_ is not None and (callable(filter_) and filter_(mergedMessage)) == False:
                continue
            
            logger.log(message=mergedMessage, option=option)
                

    @classmethod
    def getSelectorLevel(cls, levels: list):
        def filter(message: dict) -> bool:
            return ("level" in message) and message["level"] in levels
        return filter