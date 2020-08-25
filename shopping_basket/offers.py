#
# ECS code challenge
# August 2020
#

from enum import Enum


class OfferType(Enum):
    """Type of offer, multibuy or regular discount"""
    multibuy = 1
    discount = 2


class Offer:
    __slots__ = ["item", "offertype", "discount"]

    def __init__(self):
        self.item = ""  # Should match the item name. In the real world this would be done on barcode.
        self.offertype = None
        self.discount = ""
