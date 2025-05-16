# Question1 - Ali
class Rectangle:
    def __init__(self, yukseklik, genislik):     # area= Alan    # perimeter=cevresi
        self.yukseklik= yukseklik
        self.genislik= genislik

    def area(self):
        return "Dikdortgenin alani {}'dir.".format(self.yukseklik * self.genislik)
                # f"Dikdortgenin alani {self.yukseklik*self.genislik} 'dir."
    def perimeter(self):
        return "Dikdortgenin cevresi {} 'dir.".format(2*(self.yukseklik + self.genislik))
    
d= Rectangle(7, 5)    

print(d.area())
print(d.perimeter())
