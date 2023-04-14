from abc import ABC, abstractmethod

class ProductFactory(ABC):
    @abstractmethod
    def create_product(self, name, price):
        pass