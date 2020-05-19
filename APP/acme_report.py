
'''
from APP.acme import Product
from random import randint, sample, uniform

adj = ['Awesome', 'Shiny', 'Impressive','Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise','Mousetrap', '???']

def generate_products(num_products=30):
    products_names = [random.choice(adj)+ ' ' +random.choice(noun) for _ in range (num_products)]
    products = []
    for name in products_names:
        products.append(Product(name, price=randint(5, 100), weight=randint(5, 100), flammability=uniform(0.0, 2.5)))
        
    return products
    
def generate_products(num_products=30):
    """
    Generates num_products of Product from acme.py and returns a list
    """
    products = []

    for n in range(num_products):
        name = adj[randint(0, len(adj)-1)] + " " + noun[randint(0, len(noun)-1)],
        price = randint(5, 101),
        weight = randint(5, 101),
        flammability = uniform(0.0, 2.5)

        product = Product(name,
                          price=price,
                          weight=weight,
                          flammability=flammability)

        products.append(product)

        return products

def inventory_report(products):

    unique = {}
    avg_price = 0
    avg_weight = 0
    avg_flammability = 0

    for product in products:
        avg_price += product.price,
        avg_weight += product.weight,
        avg_flammability += product.flammability

        if product.name not in unique.keys():
            unique[product.name] = 1

    avg_price = avg_price / len(products)
    avg_weight = avg_weight / len(products)
    avg_flammability = avg_flammability / len(products)

    print("Acme Inventory Report:\n")
    print(f"Unique names: {len(unique.keys())}")
    print(f"Average (mean) price: {avg_price:.2f}")
    print(f"Average weight: {avg_weight:.2f}")
    print(f"Average flammability: {avg_flammability:.2f}")

if __name__ == '__main__':
    inventory_report(generate_products())
'''

import random
from APP.acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    '''should generate a given number of products (default 30), randomly, and return them as a list'''

    products = []
    for _ in range(num_products):
        name = random.sample(ADJECTIVES, 1)[0] + " " + random.sample(NOUNS, 1)[0]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        products.append(product)

    return products

def inventory_report(products):
    '''takes a list of products, and prints a "nice" summary'''

    print("\nACME CORPORATION OFFICIAL INVENTORY REPORT")

    print("Unique product names:", len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].price
    print("Average price:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].weight
    print("Average weight:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].flammability
    print("Average flammability:", total / len(products))

if __name__ == '__main__':
    inventory_report(generate_products())