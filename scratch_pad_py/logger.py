from logger_interface import LoggerInterface

class Logger(LoggerInterface):
    logger: LoggerInterface = None
   
    @classmethod
    def setLogger(cls, logger: LoggerInterface):
        cls.logger = logger

    @classmethod
    def getLogger(cls) -> LoggerInterface:
        return cls.logger

    @classmethod
    def info(cls, message: dict, option: dict = {}):
        cls.logger.info(message, option)

    @classmethod
    def notice(cls, message: dict, option: dict = {}):
        cls.logger.notice(message, option)

    @classmethod
    def warning(cls, message: dict, option: dict = {}):
        cls.logger.warning(message, option)

    @classmethod
    def error(cls, message: dict, option: dict = {}):
        cls.logger.error(message, option)

    @classmethod
    def critical(cls, message: dict, option: dict = {}):
        cls.logger.critical(message, option)