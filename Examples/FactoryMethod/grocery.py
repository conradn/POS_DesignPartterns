from factory_method import *

grocery_factory = GroceryProductFactory()

pos1 = PointOfSale(grocery_factory)
product = pos1.sell_product("Apples", 1.50)

# show product sold
print(product.name)