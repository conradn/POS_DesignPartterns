from FactoryPattern.product_factory import ProductFactory
from FactoryPattern.grocery_product import GroceryProduct

class GroceryProductFactory(ProductFactory):
    def create_product(self, name, price):
        return GroceryProduct(name, price)
