# Question4 - Kursad

class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Make: {self.make}  Model: {self.model}  Year:{self.year}  "

class Off_Road_Vehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive = True):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def get_info(self):
        return super().get_info() + f"Four Wheel Drive: {self.four_wheel_drive}"

class Sports_Car(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def get_info(self):
        return super().get_info() + f"Max Speed: {self.max_speed}"

suv = Off_Road_Vehicle("Jeep", "Wrangler", 2022)
sc = Sports_Car("Ferrari", "488 GTB", 2021, 330)

print(suv.get_info())
print(sc.get_info())