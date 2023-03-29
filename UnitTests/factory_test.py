import unittest

from FactoryPattern.point_of_sale import PointOfSale
from FactoryPattern.grocery_factory import GroceryProductFactory
from FactoryPattern.grocery_product import GroceryProduct

class TestPointOfSale(unittest.TestCase):
    def test_grocery_product_creation(self):
        grocery_factory = GroceryProductFactory()
        pos = PointOfSale(grocery_factory)

        product = pos.sell_product("Apples", 1.50)

        self.assertIsInstance(product, GroceryProduct)
        self.assertEqual(product.get_name(), "Apples")
        self.assertEqual(product.get_price(), 1.50)


if __name__ == "__main__":
    unittest.main()
