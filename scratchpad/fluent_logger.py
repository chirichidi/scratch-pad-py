from .logger_impl import LoggerImpl


from fluent import sender

class FluentLogger(LoggerImpl):
    def __init__(self, config: dict = {}):

        if "host" not in config:
            config["host"] = "localhost"
        
        if "port" not in config:
            config["port"] = 24224

        if "tag" not in config:
            config["tag"] = "scratch-pad-python"
            
        self.config = config
        self.client = None


    def log(self, message: dict, option: dict = {}):
        if self.client is None:
            self.client = sender.FluentSender(self.config["tag"], host=self.config["host"], port=self.config["port"])
        
        if "label" not in option:
            option["label"] = "test"

        return self.client.emit(option["label"], message)


    def __del__(self):
        try:
            self.client.close()
            self.client = None
        except:
            pass


if __name__ == "__main__":
    logger = FluentLogger()

    message = {
            "type": "fluent",
            "message": "hello world"
        }

    logger.log(message)