# Question3 - Furkan
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calc_area(self):
        return self.width * self.height

class Square(Shape):
    def calc_area(self):
        return self.width * self.width

rectangle = Rectangle(width=5, height=10)
square = Square(width=4, height=4)

rectangle_area = rectangle.calc_area()
square_area = square.calc_area()
print(rectangle_area, square_area)