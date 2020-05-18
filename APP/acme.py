'''
Everything Acme sells is considered a `Product`
- `name` (string with no default)
- `price` (integer with default value 10)
- `weight` (integer with default value 20)
- `flammability` (float with default value 0.5)
- `identifier` (integer, automatically genererated as a random (uniform) number
  anywhere from 1000000 to 9999999, includisve)(inclusive).
'''

from random import randint

class Product():
    def __init__(self, name, price=10,
    weight=20, flammability=0.5,
    identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammabiltity = flammability
        self.identifier = identifier

if __name__ == "__main__":
    prod = Product('A cool toy')
    print(prod.name)
    print(prod.identifier)       
'''
    def drive(self):
        print("WE ARE DRIVING", self.model)

    def advertise(self):
        print("BUY OUR", self.model)

class Truck(Auto): # designates the Truck class should inherit from the Auto class
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels) # can invoke parent class methods via super()
        self.bed_size = bed_size

    # can overwrite parent class methods
    def advertise(self):
        print("VROOOOM", self.model)

if __name__ == "__main__":

    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    car.drive()
    car.advertise()

    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car2.drive()
    car2.advertise()

    truck = Truck("Ford", "F150", 2020, "Blue", 4, bed_size="5x5")
    truck.drive()
    truck.advertise()
    print(truck.bed_size)

    truck2 = Truck("Tesla", "Cybertuck", 2020, "Blue", 4, bed_size="10x10")
    truck2.drive()
    truck2.advertise()
    print(truck2.bed_size)
    '''