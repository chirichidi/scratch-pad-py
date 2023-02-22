from .logger_impl import LoggerImpl


class MemoryLogger(LoggerImpl):

    def __init__(self):
        self.logs = []

    def log(self, message: dict, option: dict = None):
        self.logs.append(message)

    def getInMomory(self):
        return self.logs