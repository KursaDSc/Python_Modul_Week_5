# Question2 - Ali
class Okul:
    def __init__(self, isim, kurulus_yili):
        self.isim= isim
        self.kurulus_yili= kurulus_yili
        self.ogrenciler= []
        self.ogretmenler= {}

    def add_new_student(self, ad, sinif):
        ogrenci_ekle= {"isim": ad, "sinifi": sinif}
        self.ogrenciler.append(ogrenci_ekle)

    def add_new_teacher(self, ad, branch):
        ogretmen_ekle= {"isim" : ad, "bolumu" : branch}
        self.ogretmenler.update(ogretmen_ekle)

    def view_student_list(self):
        for ogrenci in self.ogrenciler:
            print(f"Adi: {ogrenci['isim']}, Sinifi: {ogrenci['sinifi']}'dir.")

    def view_teacher_list(self):  # Dikkat, bu bir sozluk. o nedenle items kullan!!
        for isim, bolumu in self.ogretmenler.items():
            print(f"Ad: {isim}, Ana_dal: {bolumu} ")


# Okul nesnesi olusturdk:
okul=Okul("Cebesoy Ilkokulu", 1990)

#Ogrenci ekleme:
okul.add_new_student= ("Ali Kilic", "1C")
okul.add_new_student= ("Sedef Atli", "3A")
okul.add_new_student= ("Murat Koc", "5K")

#ogretmen ekle:
okul.add_new_teacher=("Sahin Menevse", "Sinif")
okul.add_new_teacher=("Ozge Dal", "Matematik")

#listeleri goruntuleme:
okul.view_student_list()
okul.view_teacher_list()