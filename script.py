class Geometry:
    name = "Geometry"

    def __init__(self, x1, y1, x2, y2):
        print(f"Initializator Geometry for {self.__class__} class")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2



class Line(Geometry):
    def draw(self):
        print("Drawing a line")

class Rectangle(Geometry):
    def __init__(self, x1, y1, x2, y2, fill = None):
        super().__init__(x1, y1, x2, y2)
        print("Initializator Rectangle")
        self.fill = fill

    def draw(self):
        print("Drawing a rectangle")



r = Rectangle(2, 3, 4, 5, "Blue")
l = Line(1, 2, 3, 4)