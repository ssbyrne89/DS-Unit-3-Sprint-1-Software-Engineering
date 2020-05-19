
import unittest
from APP.acme import Product
from APP.acme_report import generate_products, adj, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_product_weight(self):
        
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        all_possible_names = []
        for adjective in adj:
            for nouns in noun:
                all_possible_names.append(adjective + " " + nouns)

        products = generate_products()
        for product in products:
            self.assertIn(product.name, all_possible_names)

if __name__ == '__main__':
    unittest.main()