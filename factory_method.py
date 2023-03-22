# Define abstract classes and interfaces
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass

class ProductFactory(ABC):
    @abstractmethod
    def create_product(self, name, price):
        pass

# Define concrete classes that implement the abstract classes/interfaces
class GroceryProduct(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

class GroceryProductFactory(ProductFactory):
    def create_product(self, name, price):
        return GroceryProduct(name, price)

class ElectronicsProduct(Product):
    def __init__(self, name, price, warranty):
        self.name = name
        self.price = price
        self.warranty = warranty
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_warranty(self):
        return self.warranty

class ElectronicsProductFactory(ProductFactory):
    def create_product(self, name, price, warranty):
        return ElectronicsProduct(name, price, warranty)

# Define the client code that uses the factories to create products
class PointOfSale:
    def __init__(self, product_factory):
        self.product_factory = product_factory
    
    def sell_product(self, name, price, *args):
        product = self.product_factory.create_product(name, price, *args)
        return product

# Example usage
grocery_factory = GroceryProductFactory()
electronics_factory = ElectronicsProductFactory()

pos1 = PointOfSale(grocery_factory)
pos1.sell_product("Apples", 1.50)

pos2 = PointOfSale(electronics_factory)
pos2.sell_product("Laptop", 999.99, "2-year warranty")
