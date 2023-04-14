from DecoratorPattern.product_decorator import ProductDecorator

class DiscountDecorator(ProductDecorator):
    def __init__(self, product, discount):
        super().__init__(product)
        self.discount = discount

    def get_price(self):
        return self.product.get_price() - self.discount
    