from DataValidators import DataValidator
import re


class PhoneNumberValidator(DataValidator):
    def _validate_data(self, data):
        match = re.fullmatch(r"^\+\d{1,3}\d{6,12}$", data)

        if not match:
            raise ValueError("Input the international number standard, please.")

        return data