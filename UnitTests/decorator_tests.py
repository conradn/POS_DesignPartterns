import unittest
from DecoratorPattern.discount_decorator import DiscountDecorator
from DecoratorPattern.tax_decorator import TaxDecorator
from FactoryPattern.point_of_sale import PointOfSale
from FactoryPattern.grocery_factory import GroceryProductFactory

class TestProduct(unittest.TestCase):

    def test_basic_product(self):
        pos = PointOfSale(GroceryProductFactory())
        product = pos.sell_product('Apple', 1.99)
        
        self.assertEqual(product.get_name(), 'Apple')
        self.assertEqual(product.get_price(), 1.99)

    def test_discount_decorator(self):
        pos = PointOfSale(GroceryProductFactory())
        product = pos.sell_product('Apple', 1.99)
        discounted_product = DiscountDecorator(product, 0.1)
        self.assertEqual(discounted_product.get_name(), 'Apple')
        self.assertEqual(discounted_product.get_price(), 1.89)


    def test_tax_decorator(self):
        pos = PointOfSale(GroceryProductFactory())
        product = pos.sell_product('Apple', 1.99)
        taxed_product = TaxDecorator(product, 0.1)
        self.assertEqual(taxed_product.get_name(), 'Apple')
        self.assertEqual(taxed_product.get_price(), 2.09)

    def test_discount_and_tax_decorator(self):
        pos = PointOfSale(GroceryProductFactory())
        product = pos.sell_product('Apple', 1.99)
        discounted_product = DiscountDecorator(product, 0.1)
        taxed_product = TaxDecorator(discounted_product, 0.1)
        self.assertEqual(taxed_product.get_name(), 'Apple')
        self.assertEqual(taxed_product.get_price(), 1.99)



if __name__ == '__main__':
    unittest.main()
