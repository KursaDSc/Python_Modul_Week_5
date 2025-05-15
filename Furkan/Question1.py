# Question1 - Furkan
class Rectangle:
    def __init__(self, width, height): #<-- "__init__" meselesini anlamadim
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
# ucgen sinifinin ornegini olustur
rectangle = Rectangle(5, 7)
#alani ve cevresini yazdir
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()

print(f"Alan: {rectangle_area}, Cevre: {rectangle_perimeter}")