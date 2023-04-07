import unittest
from SingleTonPattern.cart import Cart
class TestCart(unittest.TestCase):

    def test_singleton(self):
        cart1 = Cart.get_instance()
        cart2 = Cart.get_instance()
        self.assertIs(cart1, cart2)

    def test_add_product(self):
        cart = Cart.get_instance()
        product = {'name': 'Apple', 'price': 1.99}
        cart.add_product(product)
        self.assertIn(product, cart.products)


    def test_raise_exception(self):
        with self.assertRaises(Exception):
            cart1 = Cart()
            cart2 = Cart()

    def test_remove_product(self):
        cart = Cart.get_instance()
        product = {'name': 'Apple', 'price': 1.99}
        cart.add_product(product)
        cart.remove_product(product)
        self.assertNotIn(product, cart)

    def test_get_total(self):
        cart = Cart.get_instance()
        product1 = {'name': 'Apple', 'price': 1}
        product2 = {'name': 'Banana', 'price': 2}
        cart.add_product(product1, product2)
        self.assertEqual(cart.get_total(), 3) 

     

if __name__ == '__main__':
    unittest.main()
