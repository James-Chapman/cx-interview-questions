#
# ECS code challenge
# August 2020
#

from basket_pricer import *
from catalogue import *
from offers import *


def GetTestCatalogue():
    catalogue = Catalogue()

    category_fruit = Category()
    category_fruit.name = "Fruit"
    category_veg = Category()
    category_veg.name = "Veg"
    category_softDrink = Category()
    category_softDrink.name = "Soft drinks"
    category_alcohol = Category()
    category_alcohol = "Alcohol"

    size_s = Size()
    size_s.indicator = "S"

    size_m = Size()
    size_m.indicator = "M"

    size_l = Size()
    size_l.indicator = "L"

    # Add some items to the Catalogue
    item1 = Item()
    item1.name = "Pear"
    item1.category = category_fruit
    item1.size = size_l
    item1.price = 50
    catalogue.items.append(item1)

    item2 = Item()
    item2.name = "Bananas"
    item2.category = category_fruit
    item2.size = size_m
    item2.price = 200
    catalogue.items.append(item2)

    item3 = Item()
    item3.name = "Cucumber"
    item3.category = category_veg
    item3.size = size_m
    item3.price = 50
    catalogue.items.append(item3)

    item4 = Item()
    item4.name = "Onions (Pack of 3)"
    item4.category = category_veg
    item4.size = size_m
    item4.price = 130
    catalogue.items.append(item4)

    item5 = Item()
    item5.name = "Tonic water"
    item5.category = category_softDrink
    item5.size = size_m
    item5.price = 50
    catalogue.items.append(item5)

    item6 = Item()
    item6.name = "Tonic water"
    item6.category = category_softDrink
    item6.size = size_l
    item6.price = 90
    catalogue.items.append(item6)

    item7 = Item()
    item7.name = "Onions (Pack of 3)"
    item7.category = category_veg
    item7.size = size_m
    item7.price = 130
    catalogue.items.append(item7)

    item8 = Item()
    item8.name = "Apple"
    item8.category = category_fruit
    item8.size = size_l
    item8.price = 90
    catalogue.items.append(item8)

    item9 = Item()
    item9.name = "Apple"
    item9.category = category_fruit
    item9.size = size_m
    item9.price = 70
    catalogue.items.append(item9)

    item10 = Item()
    item10.name = "Apple"
    item10.category = category_fruit
    item10.size = size_s
    item10.price = 50
    catalogue.items.append(item10)

    # Add some offers to the Catalogue
    offer1 = Offer()
    offer1.offertype = OfferType.multibuy
    offer1.item = "Tonic water"
    offer1.discount = "2-for-1"
    catalogue.offers.append(offer1)

    offer2 = Offer()
    offer2.offertype = OfferType.discount
    offer2.item = "Cucumber"
    offer2.discount = "20"
    catalogue.offers.append(offer2)

    offer3 = Offer()
    offer3.offertype = OfferType.multibuy
    offer3.item = "Apple"
    offer3.discount = "3-for-2"
    catalogue.offers.append(offer3)

    return catalogue


def test_CalculateBasketPrice_All_Items():
    catalogue = GetTestCatalogue()

    basket = Basket()
    for item in catalogue.items:
        basket.addItem(item)

    basket = ApplyOffersToBasket(catalogue, basket)
    assert basket.total < basket.subtotal # subtotal should be less than total because discount
    assert basket.total == 800 # price in pence/cents
    assert basket.subtotal == 910 # price in pence/cents


def test_CalculateBasketPrice_Single_Item_Discount():
    catalogue = GetTestCatalogue()

    basket = Basket()
    for item in catalogue.items:
        # Let's buy 5 cucumbers because they're 20% off.
        if item.name == "Cucumber":
            basket.addItem(item)
            basket.addItem(item)
            basket.addItem(item)
            basket.addItem(item)
            basket.addItem(item)

    basket = ApplyOffersToBasket(catalogue, basket)
    for item in basket.items:
        if item.name == "Cucumber":
            assert item.price == 40


def test_CalculateBasketPrice_Multibuy_Considering_Size():
    catalogue = GetTestCatalogue()

    basket = Basket()
    for item in catalogue.items:
        if item.name == "Apple":
            basket.addItem(item)

    basket = ApplyOffersToBasket(catalogue, basket)
    for item in basket.items:
        if item.size.indicator == "S":
            assert item.price == 0
        if item.size.indicator == "M":
            assert item.price == 70
        if item.size.indicator == "L":
            assert item.price == 90


def test_GetBasketTotals():
    catalogue = GetTestCatalogue()

    basket = Basket()
    for item in catalogue.items:
        basket.addItem(item)
        if item.name == "Apple":
            basket.addItem(item)
            basket.addItem(item)
        if item.name == "Cucumber":
            basket.addItem(item)
            basket.addItem(item)

    basket = ApplyOffersToBasket(catalogue, basket)
    subtotal, saving, total = GetBasketTotals(basket)

    assert subtotal == 14.3
    assert saving == 1.3
    assert total == 13
