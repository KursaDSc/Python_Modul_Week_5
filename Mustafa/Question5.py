# Question5 - Mustafa
class Musteri:
    def __init__(self, isim, soyad, tc_kimlik, telefon):
        self.isim = isim
        self.soyad = soyad
        self.tc_kimlik = tc_kimlik
        self.telefon = telefon
    
    def musteri_bilgi_goruntule(self):
        print(f"Müşterinin Adı: {self.isim}"
              f"Müşterinin Soyadı: {self.soyad}"
              f"Müşterinin Tc. Kimlik No: {self.tc_kimlik}" 
              f"Müşterinin Telefonu: {self.telefon}"
            )
            
class Hesap(Musteri):
    def __init__(self, musteri, hesap_numarasi, bakiye=0):
        super().__init__(musteri.isim, 
                         musteri.soyad, 
                         musteri.tc_kimlik, 
                         musteri.telefon)
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_ekle(self, eklenecek_tutar):
        if eklenecek_tutar > 0:
            self.bakiye += eklenecek_tutar

    def para_cekme(self, cekilecek_tutar):
        if cekilecek_tutar > self.bakiye:
            print("Yetersiz Bakiye")
            return
        else:
            self.bakiye -= cekilecek_tutar

    def bakiye_goruntule(self):
        print (self.bakiye)

musteri1 = Musteri('Ahmet', 'TAYLAN', 12345678901, 5353355666)
hesap1 = Hesap(musteri1, 'TR09000120000035')

musteri1.musteri_bilgi_goruntule()
hesap1.para_ekle(1000)
hesap1.bakiye_goruntule()
hesap1.para_cekme(1100)
hesap1.bakiye_goruntule()
hesap1.para_cekme(600)
hesap1.bakiye_goruntule()

    
