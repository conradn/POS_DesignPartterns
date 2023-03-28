from decorator_method import *
from factory_method import *
pos = PointOfSale(GroceryProductFactory())
x = pos.sell_product("Apples", 1.50)

taxed_product = TaxDecorator(x, 0.1)
discounted_product = DiscountDecorator(x, 0.1)

print( "Actual price:",x.get_price())
print("Discounted Price:",discounted_product.get_price()) 
print("Taxed price:",taxed_product.get_price()) 
