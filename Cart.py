class ShoppingCart:
    def __init__(self):
        self._items=[]

    def add_item(self,item):
        self._items.append(item)

    def get_items(self):
        return self._items