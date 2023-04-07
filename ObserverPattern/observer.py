class Product:
    def __init__(self,product):
        self.name = product.get_name()
        self.price = product.get_price()
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self.name,self.price)

    def set_price(self, new_price):
        self.price = new_price
        self.notify()
