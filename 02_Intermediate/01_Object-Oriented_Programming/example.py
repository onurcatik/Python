# Define the Car class
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


my_car = Car("Toyota", 2020, "red", True)


my_car.describe() 
my_car.drive()     
my_car.stop() 

#  -----------------------


car1 = Car("Mustang", 2024, "Red", False)
car2 = Car("Corvette", 2025, "Blue", True)
car3 = Car("Charger", 2026, "Yellow", True)


print(car1.model) 
print(car2.year)   
print(car3.color) 
