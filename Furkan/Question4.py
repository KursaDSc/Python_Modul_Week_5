# Question4 - Furkan
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed
suv = OffRoadVehicle(make="Honda", model="CR-V", year=2023, four_wheel_drive=True)
sports_car = SportsCar(make="Ford", model="Mustang", year=2023, max_speed=250)

print("(SUV):")
print(f"Make: {suv.make}")
print(f"Model: {suv.model}")
print(f"Year: {suv.year}")
print(f"Four Wheel Drive: {suv.four_wheel_drive}")

print("\nSpor:")
print(f"Make: {sports_car.make}")
print(f"Model: {sports_car.model}")
print(f"Year: {sports_car.year}")
print(f"Max Speed: {sports_car.max_speed}")
