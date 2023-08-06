from typing import Callable
import random

class Collection:
    def __init__(self, items: list):
        self._items = items
        self._index = 0

    def __iter__(self):
        self._index = -1
        return self

    def count(self) -> int:
        """
        gets the number of total elements in the list
        """
        return len(self._items)

    def json(self) -> list:
        """
        jsonifies the list
        """
        return self._items

    def find(self, callback: Callable):
        """
        returns the first item that match with the callback
        """

        for element in self:
            if callback(element):
                return element

    def where(self, callback: Callable):
        """
        returns a new collection that meets the callback
        """

        items = []

        for item in self._items:
            if callback(self.item(item)):
                print(item)
                items.append(item)

        return self.__class__(items)

    def item(self, item):
        """
        transforms each of the list element when ite
        """
        return item

    def first(self):
        """
        gets the first item of the list
        """
        return self.item(self._items[0])

    def get(self, index:int):
        return self.item(self._items[index])

    def random(self):
        index = random.randrange(len(self._items))
        return self.get(index)

    def append(self, element):
        """
        add a new element to the list
        """
        self._items.append(element)

    def items(self) -> list:
        """
        retrieves the collection list
        """
        return self._items

    def __next__(self):
        self._index += 1
    
        if self._index < len(self._items):
            return self.item(self._items[self._index])
            
        self._index = -1
        
        raise StopIteration