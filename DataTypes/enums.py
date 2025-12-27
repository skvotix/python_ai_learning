from enum import Enum
from constants import *

class Attempt(Enum):
    SUCCEED = JSON_SUCCEED_ATTEMPTS_KEY
    ERROR = JSON_ERROR_ATTEMPTS_KEY
    FIXED = JSON_FIXED_ERROR_ATTEMPTS_KEY

    DEFAULT = JSON_ATTEMPTS_KEY


class MessageType(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"


class Status(Enum):
    SUCCESS = "success"
    ERROR = "error"