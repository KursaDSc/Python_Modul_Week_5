# Question4 - Ali
class Arac:
    def __init__(self, marka, model, yil):
        self.marka= marka
        self.model= model
        self.yil= yil

    def ozellikler(self):
        print(f"Arac Markasi: {self.marka}, Model: {self.model}, Yil: {self.yil}")    

class Suv(Arac):
    def __init__(self, marka, model, yil, dort_cekis):
        super().__init__(marka, model, yil)    
        self.dort_cekis= dort_cekis

    def ozellikler(self):
        super().ozellikler()
        print(f"Cekis ozelligi: {self.dort_cekis}")


class SporCar(Arac):
    def __init__(self, marka, model, yil, max_speed):
        super().__init__(marka, model, yil) 
        self.max_speed= max_speed       

    def ozellikler(self):
        super().ozellikler()
        print(f"Maximum hiz: {self.max_speed}")    

        
arac=Arac("Bmw", "M5", 2020)     
suv= Suv("Toyota", "Rav4", 2024, "4x4")
spor= SporCar("Subaru", "Insight", 2018, 280)

arac.ozellikler()
suv.ozellikler()
spor.ozellikler()


