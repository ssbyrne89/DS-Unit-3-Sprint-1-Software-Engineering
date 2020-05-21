

import random
from APP.acme import Product

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    '''randomly generates a products list of 30 items'''

    products = []
    for _ in range(num_products):
        name = random.sample(adj, 1)[0] + " " + random.sample(noun, 1)[0]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price, weight, flammability)
        products.append(product)

    return products

def inventory_report(products):

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(len(set(prod.name for prod in products)))
    

    total = 0
    for i in range(len(products)):
        total += products[i].price
    print("Avg price:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].weight
    print("Avg weight:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].flammability
    print("Avg flammability:", total / len(products))

if __name__ == '__main__':
    inventory_report(generate_products())