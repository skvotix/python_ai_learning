from DataValidators import DataValidator
from DataTypes.dataclasses import Error

class Dialog:
    def ask_data(self, text: str, validator: DataValidator):
        self.write(text, " ")
        result = validator.validate(self.read())

        if isinstance(result, Error):
            self.write(result.error_text)
            return self.ask_data(text, validator)

        return result


    @staticmethod
    def read():
        return input()

    @staticmethod
    def write(value: str, end = "\n"):
        print(value, end = end)
