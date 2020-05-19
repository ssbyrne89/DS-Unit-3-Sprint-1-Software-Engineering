from APP.acme import Product
from random import randint, sample, uniform, choice
import random

adj = ['Awesome', 'Shiny', 'Impressive','Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise','Mousetrap', '???']

def generate_products(num_products=30):
    products_names = [random.choice(adj)+ ' ' +random.choice(noun) for _ in range (num_products)]
    products = []
    for name in products_names:
        products.append(Product(name, price=randint(5, 100), weight=randint(5, 100), flammability=uniform(0.0, 2.5)))
        
    return products
        

def inventory_report(products):

    print(f"\nACME CORPORATION OFFICIAL INVENTORY REPORT")

    print(f"Unique product names:", len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].price
    print(f"Avg. price:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].weight
    print(f"Avg. weight:", total / len(products))

    total = 0
    for i in range(len(products)):
        total += products[i].flammability
    print(f"Avg. flammability:", total / len(products))

if __name__ == '__main__':
    inventory_report(generate_products())