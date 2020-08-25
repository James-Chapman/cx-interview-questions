#
# ECS code challenge
# August 2020
#
from basket import *
from offers import *


def ApplyOffersToBasket(catalogue, basket):
    newBasket = Basket()
    basketItems = dict()

    # Build a hash map of items to make applying the discounts easier an more efficient
    for item in basket.items:
        basket.subtotal += item.price
        if item.name in basketItems:
            basketItems[item.name].append(item)
        else:
            basketItems[item.name] = []
            basketItems[item.name].append(item)

    # Iterate over the offers and see which apply to the items in the basket
    for offer in catalogue.offers:
        if offer.item in basketItems:
            # Multibuy offers require a bit more work
            if offer.offertype == OfferType.multibuy:
                itemCount = len(basketItems[offer.item])
                t = offer.discount.split("-for-")
                if itemCount >= int(t[0]):
                    itemsToReduce = int(t[0]) - int(t[1])
                    # discount the smallest first
                    for item in basketItems[offer.item]:
                        if item.size.indicator == "S" and itemsToReduce > 0:
                            item.price = 0
                            itemsToReduce -= 1
                    for item in basketItems[offer.item]:
                        if item.size.indicator == "M" and itemsToReduce > 0:
                            item.price = 0
                            itemsToReduce -= 1
                    for item in basketItems[offer.item]:
                        if item.size.indicator == "L" and itemsToReduce > 0:
                            item.price = 0
                            itemsToReduce -= 1
            # Discount offers are easy to apply to the relevant items
            if offer.offertype == OfferType.discount:
                for item in basketItems[offer.item]:
                    item.price -= (item.price / 100) * int(offer.discount)

    # Add discounted items to the new basket
    for k in basketItems.keys():
        for item in basketItems[k]:
            newBasket.addItem(item)
            newBasket.total += item.price

    # Return a new discounted basket
    newBasket.subtotal = basket.subtotal
    print("Subtotal: %.2f" % (float(newBasket.subtotal / 100)))
    print("Total: %.2f" % (float(newBasket.total / 100)))
    print("Saved: %.2f" % (float((newBasket.subtotal - newBasket.total) / 100)))

    return newBasket


def GetBasketTotals(basket):
    return (float(basket.subtotal / 100)), float((basket.subtotal - basket.total) / 100), float(basket.total / 100)
