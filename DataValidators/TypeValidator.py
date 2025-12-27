from DataValidators import DataValidator

class TypeValidator(DataValidator):
    def _validate_data(self, data):
        try:
            self._type(data)
            return data
        except:
            raise TypeError(f"Wrong type. Expected a {self._type} got {type(data)}.")



