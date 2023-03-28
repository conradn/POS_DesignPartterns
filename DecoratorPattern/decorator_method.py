from factory_method import *

class ProductDecorator(Product):
    def __init__(self, product):
        self.product = product

    def get_name(self):
        return self.product.get_name()

    def get_price(self):
        return self.product.get_price()
    

class DiscountDecorator(ProductDecorator):
    def __init__(self, product, discount):
        super().__init__(product)
        self.discount = discount

    def get_price(self):
        return self.product.get_price() - self.discount
    


class TaxDecorator(ProductDecorator):
    def __init__(self, product, tax):
        super().__init__(product)
        self.tax = tax

    def get_price(self):
        return self.product.get_price() + self.tax