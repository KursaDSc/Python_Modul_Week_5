# Question1 - Mustafa
class Rectangle:
    def __init__(self, genislik, yukseklik ):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan(self):
        return self.genislik * self.yukseklik
    
    def cevre(self):
        return 2 * (self.genislik + self.yukseklik)

diktortgen = Rectangle(5,7)
print(diktortgen.alan())
print(diktortgen.cevre())

        