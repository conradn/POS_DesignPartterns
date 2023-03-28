class Cart:
    __instance = None

    def __init__(self):
        if Cart.__instance is not None:
            raise Exception(
                "Singleton class, use get_instance() method to get instance.")
        else:
            Cart.__instance = self
            self.products = []

    @staticmethod
    def get_instance():
        if Cart.__instance is None:
            Cart()
        return Cart.__instance

    def product_details(self, name, price):
        return {'name': name, 'price': price}

    def add_product(self, *product_list):
        for product in product_list:
            self.products.append(product)
        

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products

    def get_total(self):
        total = 0
        for i in self.products:
            total += i['price']

        return total


c = Cart().get_instance()

product1 = c.product_details('Apple', 9000)
product2 = c.product_details('Apple', 6000)
product3 = c.product_details('Apple', 1000)
product4 = c.product_details('Apple', 5000)

print('before adding\n')
c.add_product(product1,product2)
print('after adding\n')
print(c.get_products())
print('on removing\n')
print(c.remove_product(product1))
print('after removing\n')
print(c.get_products())
