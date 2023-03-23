import unittest
from singletonPattern import *
class TestCart(unittest.TestCase):

    def test_singleton(self):
        cart1 = Cart.get_instance()
        cart2 = Cart.get_instance()
        self.assertIs(cart1, cart2)

    def test_add_product(self):
        cart = Cart.get_instance()
        product = {'name': 'Apple', 'price': 1.99}
        cart.products.append(product)
        self.assertIn(product, cart.products)

    def test_raise_exception(self):
        with self.assertRaises(Exception):
            cart1 = Cart()
            cart2 = Cart()

if __name__ == '__main__':
    unittest.main()
