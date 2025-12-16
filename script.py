class FRange:
    def __init__(self, start = 0.0, stop = 0.0, step = 1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.__value = self.start - self.step


    def __iter__(self):
        self.__value = self.start - self.step
        return self

    def __next__(self):
        if self.__value + self.step < self.stop:
            self.__value += self.step
            return self.__value
        else:
            raise StopIteration

fr = FRange(0, 2, 0.5)

it = iter(fr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

it = iter(fr)

print(next(it))
print(next(it))
print(next(it))
print(next(it))