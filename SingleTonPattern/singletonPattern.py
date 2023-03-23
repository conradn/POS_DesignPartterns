class Cart:
    __instance = None

    def __init__(self):
        if Cart.__instance is not None:
            raise Exception("Singleton class, use get_instance() method to get instance.")
        else:
            Cart.__instance = self
            self.items = []
    
    @staticmethod
    def get_instance():
        if Cart.__instance is None:
            Cart()
        return Cart.__instance
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def get_items(self):
        return self.items
