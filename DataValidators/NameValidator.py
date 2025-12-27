from DataValidators import DataValidator

class NameValidator(DataValidator):
    def _validate_data(self, data: str):
        parts = data.strip().split()

        if len(parts) < 2:
            raise ValueError("Type a name with firstname and lastname at least, please.")

        return data