from DataValidators import DataValidator

class MessageTypeValidator(DataValidator):
    def _validate_data(self, data: str):
        if data.lower().strip() not in ("email", "sms", "push"):
            raise ValueError("Not an option. Pick between given options, please.")

        return data