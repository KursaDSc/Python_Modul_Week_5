# Question5 - Ali
class Musteri:
    def __init__(self, isim, soyad, Tc, telefon):
        self.isim= isim
        self.soyad= soyad 
        self.Tc= Tc
        self.telefon= telefon

    def hesap_bilgileri(self):
        print(f"Musteri Adi: {self.isim}, Soyadi: {self.soyad}, Tc no: {self.Tc}, Telfn: {self.telefon}")
        # print(f"Müşteri Adı: {self.isim} {self.soyad}")
        # print(f"TC: {self.Tc}")
        # print(f"Telefon: {self.telefon}")

class Hesap(Musteri):
    def __init__(self, musteri, hesap_no, bakiye):
        super().__init__(musteri.isim, musteri.soyad, musteri.Tc, musteri.telefon)     
        self.musteri= musteri
        self.hesap_no= hesap_no
        self.bakiye= bakiye

    def deposit(self, miktar):
        self.bakiye += miktar
        print(f"Hesaba {miktar} Tl para yatirilmistir. Guncel bakiyniz: {self.bakiye} Tldir.")

    def money_check(self, miktar):
        if self.bakiye >= miktar:
            self.bakiye -= miktar
            print(f"Hesabinizdan {miktar} Tl cekilmistir. Yeni bakiyeniz {self.bakiye} Tl dir.")
        else:
            print("Bakiyeniz yetersiz!")

    def bakiye_goruntule(self):
        print(f"Bakiyeniz: {self.bakiye} dir.")

# Nesneler:
        
musteri1= Musteri("Hasan", "Kaya", 12536896547, "05368659986")
musteri2= Musteri("Salih", "Kocak", 45562633563, "05326632578" )
hesap1= Hesap(musteri1, 125456332, 7000)
hesap2= Hesap(musteri2, "INGB52378523", 12000)


musteri1.hesap_bilgileri()
musteri2.hesap_bilgileri()
musteri1.soyad
hesap2.hesap_bilgileri()
hesap1.bakiye_goruntule()
hesap2.deposit(300)
hesap1.money_check(1000)


