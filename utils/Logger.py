import json

from constants import *
from DataTypes.enums import Attempt

class Logger:
    def __init__(self, filename: str):
        self.__filename = filename

    def setup(self):
        data = {
            JSON_ATTEMPTS_KEY: 0,
            JSON_SUCCEED_ATTEMPTS_KEY: 0,
            JSON_ERROR_ATTEMPTS_KEY: 0,
            JSON_FIXED_ERROR_ATTEMPTS_KEY: 0
        }

        with open(self.__filename, "w") as file:
            json.dump(data, file, indent = 4)




    def log(self, attempt: Attempt):
        self.__write(attempt.value)



    def __write(self, key: str):
        with open(self.__filename, "r") as file:
            data = json.load(file)

        data[key] += 1

        with open(self.__filename, "w") as file:
            json.dump(data, file, indent = 4)



    def send_logs(self) -> dict:
        with open(self.__filename, "r", encoding = "utf-8") as file:
            data = json.load(file)

        return data
