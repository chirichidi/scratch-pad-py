from abc import abstractmethod, ABCMeta

class LoggerInterface(metaclass=ABCMeta):
    @abstractmethod
    def log(self, message: dict, option: dict = {}):
        pass

    @abstractmethod
    def info(self, message: dict, option: dict = {}):
        pass

    @abstractmethod
    def notice(self, message: dict, option: dict = {}):
        pass

    @abstractmethod
    def warning(self, message: dict, option: dict = {}):
        pass
    
    @abstractmethod
    def error(self, message: dict, option: dict = {}):
        pass

    @abstractmethod
    def critical(self, message: dict, option: dict = {}):
        pass