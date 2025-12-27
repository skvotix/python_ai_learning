from DataTypes.dataclasses import Error

class ErrorHandler:
    @staticmethod
    def handle_error(function):
        try:
            return function()
        except Exception as e:
            return Error(e.args[0])