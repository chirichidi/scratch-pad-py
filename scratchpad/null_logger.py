from .logger_impl import LoggerImpl


class NullLogger(LoggerImpl):

    def log(message: dict, option: dict = None):
        pass