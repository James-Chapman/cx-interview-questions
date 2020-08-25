#
# ECS code challenge
# August 2020
#

class Category:
    """Category is a way of grouping items together by type"""
    __slots__ = ["name"]

    def __init__(self):
        self.name = ""


class Size:
    """Size is arbitrary and relevant to other matching items"""
    __slots__ = ["indicator"]

    def __init__(self):
        self.indicator = ""


class Item:
    """Items are things that a user would purchase"""
    __slots__ = ["name", "category", "size", "price"]

    def __init__(self):
        self.name = ""
        self.category = None
        self.size = None
        self.price = 0


class Catalogue:
    """All the items and offers available in the shop"""
    __slots__ = ["items", "offers"]

    def __init__(self):
        self.items = []
        self.offers = []
