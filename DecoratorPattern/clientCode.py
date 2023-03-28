from decorator_method import *
from factory_method import *
pos = PointOfSale(GroceryProductFactory())


product = pos.sell_product("Apples", 1.50)

taxed_product = TaxDecorator(product, 0.1)
discounted_product = DiscountDecorator(product, 0.5)

print( "Actual price:",product.get_price())
print("Discounted Price:",discounted_product.get_price()) 
print("Taxed price:",taxed_product.get_price()) 
