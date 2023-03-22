import unittest

from factory_method import *

class TestPointOfSale(unittest.TestCase):
    def test_grocery_product_creation(self):
        grocery_factory = GroceryProductFactory()
        pos = PointOfSale(grocery_factory)

        product = pos.sell_product("Apples", 1.50)

        self.assertIsInstance(product, GroceryProduct)
        self.assertEqual(product.get_name(), "Apples")
        self.assertEqual(product.get_price(), 1.50)

    def test_electronics_product_creation(self):
        electronics_factory = ElectronicsProductFactory()
        pos = PointOfSale(electronics_factory)

        product = pos.sell_product("Laptop", 999.99, "2-year warranty")

        self.assertIsInstance(product, ElectronicsProduct)
        self.assertEqual(product.get_name(), "Laptop")
        self.assertEqual(product.get_price(), 999.99)
        self.assertEqual(product.get_warranty(), "2-year warranty")

if __name__ == "__main__":
    unittest.main()
