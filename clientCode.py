from DecoratorPattern.discount_decorator import DiscountDecorator
from FactoryPattern.point_of_sale import PointOfSale
from FactoryPattern.grocery_factory import GroceryProductFactory
from ObserverPattern.custormer_observer import Customer
from ObserverPattern.observer import Product
from SingleTonPattern.cart import Cart


pos = PointOfSale(GroceryProductFactory())

#product selected
oranges = pos.sell_product("Oranges", 3000)

#add to cart
cart = Cart().get_instance()

product = cart.product_details(oranges)

cart.add_product(product)

# get original total
print("Original Total")
print(cart.get_total())


#add customer
customer = Customer("Samuel")

#product bought
bought = Product(oranges)

#associate product with customer
bought.attach(customer)

#apply discount
discounted_price = DiscountDecorator(oranges, 0.5).get_price()

#notify customer of new price
bought.set_price(discounted_price)
