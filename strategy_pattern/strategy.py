from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def pay(self, amount):
        # Implement payment logic using credit card
        print(f'Paid {amount} using credit card {self.card_number}.')

class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self, amount):
        # Implement payment logic using PayPal
        print(f'Paid {amount} using PayPal account {self.email}.')

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        # Implement payment logic using cash
        print(f'Paid {amount} using cash.')

class MobileMoneyPayment(PaymentStrategy):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def pay(self, amount):
        # Implement payment logic using mobile money
        print(f'Paid {amount} using mobile money {self.phone_number}.')

class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)
