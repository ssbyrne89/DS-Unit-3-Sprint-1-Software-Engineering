from APP.acme import Product
from random import randint, sample, uniform

adj = ('Awesome', 'Shiny', 'Impressive',
'Portable', 'Improved')
noun = ('Anvil', 'Catapult', 'Disguise',
'Mousetrap', '???')

def generate_products(num_products=30):
    products_names = [random.choice(adj)+ ' ' +random.choice(noun) for _ in range (num_products)]
    products = []
    for name in products_names:
        products.append(Product(name, price=randint(5, 100), weight=randint(5, 100), flammability=uniform(0.0, 2.5)))
        
    return products


def inventory_report(products)
    products.nunique()
    for price in products:
        return(iter in range(limit)]
    pass 
    limit = 30
    name = [(random.choice(adj)+ ' ' +random.choice(noun)) for iter in range(limit)]
    

    for name in products:
        products = Product(name)
        


def inventory_report