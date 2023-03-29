import unittest
from observer import Product

class ProductTestCase(unittest.TestCase):

    def test_observer_pattern(self):

        class TestObserver:
            def __init__(self):
                self.updated_name = None
                self.updated_price = None

            def update(self, name, price):
                self.updated_name = name
                self.updated_price = price

        product = Product(ProductStub("Test Product", 10.0))

        observer1 = TestObserver()
        observer2 = TestObserver()

        product.attach(observer1)
        product.attach(observer2)

        product.set_price(20.0)

        self.assertEqual(observer1.updated_name, "Test Product")
        self.assertEqual(observer1.updated_price, 20.0)
        self.assertEqual(observer2.updated_name, "Test Product")
        self.assertEqual(observer2.updated_price, 20.0)

        product.detach(observer1)

        product.set_price(30.0)

        self.assertEqual(observer1.updated_name, "Test Product") # Should be unchanged
        self.assertEqual(observer1.updated_price, 20.0) # Should be unchanged
        self.assertEqual(observer2.updated_name, "Test Product")
        self.assertEqual(observer2.updated_price, 30.0)

class ProductStub:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

if __name__ == '__main__':
    unittest.main()
