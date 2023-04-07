from DecoratorPattern.product_interface import Product

class ProductDecorator(Product):
    def __init__(self, product):
        self.product = product

    def get_name(self):
        return self.product.get_name()

    def get_price(self):
        return self.product.get_price()
    