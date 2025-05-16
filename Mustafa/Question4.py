# Question4 - Mustafa
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        return f"Markası: {self.make} Modeli: {self.model} Yılı: {self.year}"

class Off_Road_Vehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive=True):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive
    
    def show_info(self):
        dort_ceker_mi = 'Evet' if self.four_wheel_drive else 'Hayır'
        return super().show_info() + f" Dört Çeker: {dort_ceker_mi}"

class Sport_car(Vehicle):
    def __init__(self, make, model, year, max_speed= True):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def show_info(self):
        spor_mu = 'Evet' if self.max_speed else 'Hayır'
        return super().show_info() + f" Spor: {spor_mu}"
    
duz_arac = Vehicle('Honda', 'Civic', 2021)
dort_ceker = Off_Road_Vehicle('Tesla', 'Cybertruck', 2022)
spor_arac = Sport_car('Mazda', 'MX5', 2010)

print(duz_arac.show_info())
print(dort_ceker.show_info())
print(spor_arac.show_info())
    

