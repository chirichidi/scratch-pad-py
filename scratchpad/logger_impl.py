from .logger_interface import LoggerInterface

class LoggerImpl(LoggerInterface):

    def log(self, message: dict, option: dict = None):
        if option is None:
            option = {}
        pass

    def info(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        mergedMessage = {}
        mergedMessage["level"] = "info"
        mergedMessage.update(message)
        self.log(mergedMessage, option)

    def notice(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        mergedMessage = {}
        mergedMessage["level"] = "notice"
        mergedMessage.update(message)
        self.log(mergedMessage, option)

    def warning(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        mergedMessage = {}
        mergedMessage["level"] = "warning"
        mergedMessage.update(message)
        self.log(mergedMessage, option)

    def error(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        mergedMessage = {}
        mergedMessage["level"] = "error"
        mergedMessage.update(message)
        self.log(mergedMessage, option)

    def critical(self, message: dict, option: dict = None):
        if option is None:
            option = {}

        mergedMessage = {}
        mergedMessage["level"] = "critical"
        mergedMessage.update(message)
        self.log(mergedMessage, option)