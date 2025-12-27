from utils.ErrorHandler import *
from abc import ABC, abstractmethod

class DataValidator(ABC):
    def __init__(self, error_handler: ErrorHandler = ErrorHandler(), _type: type = None):
        self._error_handler = error_handler
        self._type = _type

    @abstractmethod
    def _validate_data(self, data):
        pass

    def validate(self, data):
        return self._error_handler.handle_error(lambda: self._validate_data(data))