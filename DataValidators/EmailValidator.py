from DataValidators import DataValidator
import re

class EmailValidator(DataValidator):
    def _validate_data(self, data):
        match = re.fullmatch(r"^[\w.-]+@[\w.-]+\.\w{2,}$", data)

        if not match:
            raise ValueError("Input the email, please")

        return data