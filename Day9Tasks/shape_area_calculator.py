import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle1 = Circle(7)
rectangle1 = Rectangle(10, 5)
triangle1 = Triangle(8, 6)

shapes = [circle1, rectangle1, triangle1]

for shape in shapes:
    print(f"{type(shape).__name__} Area: {shape.area():.2f}")
    