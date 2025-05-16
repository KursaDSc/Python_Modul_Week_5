# Question3 - Mustafa
class Shape:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

class Rectangle(Shape):
    def calculate_area(self):
        return self.genislik * self.yukseklik

class Square(Rectangle):
    def __init__(self, kenar):
        super().__init__(kenar, kenar)

diktortgen = Rectangle(4,6)    
print(f"Dİktörtgenin Karesi: {diktortgen.calculate_area()}")

kare = Square(5)
print(f"Karenin alanı: {kare.calculate_area()}")
