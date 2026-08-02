class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print(f"Length: {self.length}, Width: {self.width}, Area: {area}")


rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)

rectangle1.calculate_area()
rectangle2.calculate_area()
