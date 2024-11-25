class ShoppingCart:
    def __init__(self,cart_limit):
        self._items=[]
        self._cart_limit = cart_limit

    def add_item(self,item):
        if self.get_num_items() == self._cart_limit:
            raise OverflowError("Cannot add additional items!")
        self._items.append(item)

    def get_num_items(self):
        return len(self._items)