class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_area(self):
        return self.width * self.height
    
rec = Rectangle(5,7)
print(rec.calculate_area())

sq = Square(5)
print(sq.calculate_area())