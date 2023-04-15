from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass