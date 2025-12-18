class Geometry:
    class_name = "Geometry"


    def set_coords(self, *args):
        self.coords = args

    def get_coords(self):
        return tuple(self.coords)


    def __call__(self, *args, **kwargs):
        self.set_coords(*args)


class Line(Geometry):

    def draw(self):
        print("Drawing a line")



class Rectangle(Geometry):

    def draw(self):
        print("Рисование прямоугольника")




