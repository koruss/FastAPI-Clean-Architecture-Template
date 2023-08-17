from abc import ABC, abstractmethod

class ILogger(ABC):

    @abstractmethod
    def log_warning(self, message):
        pass

    @abstractmethod
    def log_info(self, message):
        pass

    @abstractmethod
    def log_error(self, message):
        pass

    @abstractmethod
    def start(self, message):
        pass


