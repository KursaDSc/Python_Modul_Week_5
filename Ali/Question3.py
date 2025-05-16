# Question3 - Ali
class Sekil:
    def __init__(self, genislik, yukseklik):
        self.genislik= genislik
        self.yukseklik= yukseklik

    def alan(self):
        return "Alan: {}".format(self.genislik * self.yukseklik)    
        
class Dikdortgen(Sekil):
    def __init__(self, genislik, yukseklik, dikdortgen):
        super().__init__(genislik, yukseklik)
        self.dikdortgen= dikdortgen
    

class Kare(Sekil):
    def __init__(self, genislik, yukseklik, kare ):
        super().__init__(genislik, yukseklik)
        self.kare= kare 

d_dortgen= Dikdortgen(5,8,"dikdortgen")      

print(d_dortgen.alan())      

k_kare= Kare(10,10,"kare")

print(k_kare.alan())