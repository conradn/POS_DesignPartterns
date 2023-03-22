import sys
sys.path.append('../')

from factory_method import *

electronics_factory = ElectronicsProductFactory()

pos2 = PointOfSale(electronics_factory)
product = pos2.sell_product("Laptop", 999.99, "2-year warranty")

print(product);