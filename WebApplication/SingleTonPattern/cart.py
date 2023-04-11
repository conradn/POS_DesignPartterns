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

    def product_details(self,product):
        return {'name': product.get_name(), 'price': product.get_price()}

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
