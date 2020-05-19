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
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammabiltity = flammability
        self.identifier = identifier

    def stealability(self):
        x = self.price/self.weight
        if x < 0.5:
            message = 'not so stealable'
        else:
            if x >= 1.0:
                message = "very stealable"
            else:
                message = 'kinda stealable'
        
        return message

    def explode(self):
        x = self.flammabiltity * self.weight
        if x < 10:
            message = '...fizzle.'
        else:
            if x >= 50:
                message = "....BABOOM!!"
            else:
                message = '...boom!'
        
        return message
class BoxingGlove(Product):
    def __init__(self, name, price=10,
    weight=10, flammability=0.5,
    identifier=randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        print("...it's a glove")

    def punch(self):
        x = self.weight
        if x < 5:
            message = 'That tickles!'
        else:
            if x > 15:
                message = "OUCH!!"
            else:
                message = 'Hey that hurts!'
        return message


if __name__ == "__main__":
    prod = Product('A cool toy')
    print(prod.name)
    print(prod.identifier)     
