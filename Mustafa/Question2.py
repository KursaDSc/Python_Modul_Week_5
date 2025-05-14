# Question2 - Mustafa
class Okul:
    def __init__(self, isim, kurulus_yili, ogrenciler, ogretmenler):
        self.isim = isim
        self.kurulus_yili = kurulus_yili
        self.ogrenciler = ogrenciler
        self.ogretmenler = ogretmenler

    def add_new_student(self, isim, sinif):
        self.ogrenciler.append([isim, sinif])
        return self.ogrenciler
    
    def add_new_teacher(self, teacher_name, branch):
        self.ogretmenler[teacher_name] = branch
        return f"Yeni öğretmen eklendi: {teacher_name} - Branş: {branch}"

    def view_student_list(self):
        return [f"Öğrenci Adı:  {isim}, Sınıfı: {sinif}" for isim, sinif in self.ogrenciler]
    
    def view_teacher_list(self):
        return [f"Öğretmenin Adı: {isim}, Branşı: {branch}" for isim, branch in self.ogretmenler.items()]


okul = Okul('Fatih Sultan Lisesi', 2000, [], {})

yeni_ogrenci = okul.add_new_student('Ali', 'A')
print(yeni_ogrenci)

yen_ogretmen = okul.add_new_teacher('Üsame', 'İngilizce')
print(yen_ogretmen)

yeni_ogrenci = okul.add_new_student('Veli', 'B')
print(yeni_ogrenci)

ogreci_listesi = okul.view_student_list()
print(ogreci_listesi)

ogretmen_listesi = okul.view_teacher_list()
print(ogretmen_listesi)




