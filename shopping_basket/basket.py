#
# ECS code challenge August 2020
#
import copy


class Basket:
    __slots__ = ["items", "offers", "total", "subtotal", "discount"]

    def __init__(self):
        self.items = []
        self.offers = []
        self.total = 0
        self.subtotal = 0
        self.discount = 0

    def addItem(self, item):
        """Add an item to the basket"""
        # Copy because items are manipulated in the basket at checkout
        self.items.append(copy.copy(item))
