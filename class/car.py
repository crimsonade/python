class Car:
    def __init__(self, make, model, year ):
        self.make=make
        self.model=model
        self.year= year
        self.odometer_reading= 0

    def get_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, milege):
        self.odometer_reading= milege

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car= Car('ram','1500 REV',2026)
print(my_car.get_name())

#my_car.read_odometer()

my_car.update_odometer(23_500)
my_car.read_odometer()

my_car.increment_odometer(400)
my_car.read_odometer()

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size= battery_size

    def des_battery(self):
            print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size==75:
            range= 260
        elif self.battery_size == 100:
            range= 315
        print(f"This car go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery= Battery()

    
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")
    
my_tesla= ElectricCar('tesla','model s', 2019)
print(my_tesla.get_name())

my_tesla.fill_gas_tank()
my_tesla.battery.des_battery()
my_tesla.battery.get_range()