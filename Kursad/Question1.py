# Question1 - Kursad
import os

class Rectangle():
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        return self.width * self.heigth    
    
    def perimeter(self):
        return 2*(self.width + self.heigth)
    
rect = Rectangle(5,7)

os.system("cls")

print("Dikdörtgenin alanı: {}\n".format(rect.area()))
print("Dikdörtgenin çevresi: {}\n".format(rect.perimeter()))

