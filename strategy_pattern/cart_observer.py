

class CartObserver:
    def update_cart(self, name: str, quantity: int):
        pass

    
class ShoppingCart(CartObserver):
    def __init__(self):
        self.products = {}

    def update_cart(self, name: str, quantity: int):
        if name in self.products:
            self.products[name] += quantity
        else:
            self.products[name] = quantity

    def get_products(self):
        return self.products
