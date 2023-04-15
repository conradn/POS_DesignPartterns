from strategy import *
from cart_observer import *
from barcode import *
credit_card = CreditCardPayment('1234567890123456', '01/23', '123')
paypal = PayPalPayment('example@example.com', 'password')
mm = MobileMoneyPayment('+25674567890')
cash = CashPayment()

payment_context = PaymentContext(credit_card)
payment_context.pay(100)

payment_context.set_payment_strategy(paypal)
payment_context.pay(50)

payment_context.set_payment_strategy(mm)
payment_context.pay(25)

payment_context.set_payment_strategy(cash)
payment_context.pay(10)


# Create a new shopping cart
cart = ShoppingCart()

# Create a barcode scanner and pass in the shopping cart
scanner = BarcodeScanner(cart)

# Simulate scanning some products
scanner.scan("apple")
scanner.scan("mango", 2)
scanner.scan("apple",3)

# Get the updated products in the cart
print(cart.get_products())  # {'apple': 4, 'mango': 2}
