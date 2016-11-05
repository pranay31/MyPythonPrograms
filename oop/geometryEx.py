"""Create model classes that will properly represent the following constructs:

Define a Shape object, where the object is any two dimensional figure, and has the following characteristics:
a name, a perimeter, and a surface area.
Define a Circle, retaining and accurately outputting the values of the aforementioned characteristics of a Shape.
Define a Triangle. This time, the name of the triangle should take into account if it is equilateral (all 3 sides
are the same length), isosceles (only 2 sides are the same length), or scalene (no 2 sides are the same).
You can go on and on with quadrilaterals (which include squares, rectangles, rhombus, etc) and other polygons."""


class Shape(object):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        return self.name

        
class Circle(Shape):
    def __init__(self, name, r):
        super(Circle, self).__init__(name)
        self.r = r

    def circum(self):
        cir = 2 * 3.14 * self.r
        return cir

    def area(self):
        area = 3.14 * self.r**2
        return area

if __name__ == '__main__':
    circle = Circle("circle", 5)
    print circle.name
    print circle.print_name()
    print circle.r
    print circle.circum()
    print circle.area()
