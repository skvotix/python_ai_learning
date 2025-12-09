class ClassPresentator:
    def __init__(self, cls):
        self.__cls = cls

    def __call__(self, *args, **kwargs):
        print(f"Created object of class {self.__cls.__name__} with args {args}, kwargs {kwargs}")
        return self.__cls(*args, **kwargs)


@ClassPresentator
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __call__(self):
        print("Hey!")



toyota = Car("Toyota", 1999)
toyota()