class Cart:
    __instance = None

    def __init__(self):
        if Cart.__instance is not None:
            raise Exception("Singleton class, use get_instance() method to get instance.")
        else:
            Cart.__instance = self
            self.products = []
    
    @staticmethod
    def get_instance():
        if Cart.__instance is None:
            Cart()
        return Cart.__instance
    
    def add_item(self, product):
        self.products.append(product)
    
    def remove_item(self, product):
        self.products.remove(product)
    
    def get_products(self):
        return self.products
    
c = Cart().get_instance()
c.add_item("product1")
c.add_item("product2")
print(c.get_products())






    
    
        




