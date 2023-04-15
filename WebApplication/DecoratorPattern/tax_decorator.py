from DecoratorPattern.product_interface import ProductDecorator

class TaxDecorator(ProductDecorator):
    def __init__(self, product, tax):
        super().__init__(product)
        self.tax = tax

    def get_price(self):
        return self.product.get_price() + self.tax