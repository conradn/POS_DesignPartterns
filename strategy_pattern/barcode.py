from cart_observer import *

class BarcodeScanner:
    def __init__(self, cart: CartObserver):
        self.cart = cart

    def scan(self, name: str, quantity: int = 1):
        self.cart.update_cart(name, quantity)
