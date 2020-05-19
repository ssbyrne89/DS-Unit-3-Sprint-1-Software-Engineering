#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, adj, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

        def test_acme(self):
        
        df = (products)
        processor = DataProcessor(df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])

        processor.add_state_names()

        
        self.assertEqual(list(processor.df.columns), ["abbrev", "name"])
        self.assertEqual(processor.df.iloc[0]['abbrev'], "CA")
        self.assertEqual(processor.df.iloc[0]['name'], "Cali")

if __name__ == '__main__':
    unittest.main()