import socket

from .logger_impl import LoggerImpl
from fluent import sender

class FluentLogger(LoggerImpl):
    def __init__(self, config: dict = None):
        if config is None:
            config = {}

        if "host" not in config:
            config["host"] = "localhost"
        
        if "port" not in config:
            config["port"] = 24224

        if "tag" not in config:
            config["tag"] = "scratch-pad-python"
            
        self.config = config
        self.client = None
        self.check_connection()


    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}
        if self.client is None:
            self.client = sender.FluentSender(self.config["tag"], host=self.config["host"], port=self.config["port"])

        return self.client.emit(option.get("label"), message)


    def __del__(self):
        try:
            self.client.close()
            self.client = None
        except:
            pass

    def check_connection(self):
        try:
            timeout = 5
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.config["host"], self.config["port"]))
        except ConnectionRefusedError as e:
            raise e


if __name__ == "__main__":
    logger = FluentLogger()

    message = {
            "type": "fluent",
            "message": "hello world"
        }

    logger.log(message)