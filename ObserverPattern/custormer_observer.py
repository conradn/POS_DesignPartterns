from ObserverPattern.observer_interface import Observer

class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self,product_name,product_price):
        print(f"{self.name}, the price of {product_name} has changed to {product_price}")
