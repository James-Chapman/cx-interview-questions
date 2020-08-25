## Documentation

## A note on prices.
All prices are in pence/cents as integers. It's only at the final stage that the prices are converted to floats.


### Requirements: 
* pytest


### Running the tests
change directory to `cx-interview-questions/shopping_basket/shopping_basket_tests` and run `pytest -v`


### Files

#### basket_pricer.py

`ApplyOffersToBasket(catalogue, basket)`: function to calculate the subtotal and total of the shopping basket. Params are a catalogue and basket. Returns a new basket with offers applied.

`GetBasketTotals(basket)`: Gets sub-total, saving and total for a given basket.

#### shopping_basket_tests/test_basket_pricer.py

`test_CalculateBasketPrice_All_Items()`: Tests that offers and totals are correctly applied.

`test_CalculateBasketPrice_Single_Item_Discount()`: Tests that single item discounts apply to each item in the basket.

`test_CalculateBasketPrice_Multibuy_Considering_Size()`: Tests that multi-buy offers are correctly applied.

`test_GetBasketTotals`: Tests that prices are returned as floats.


#### basket.py

`Basket`: Class that represents the shopping basket.

`Basket.addItem(item)`: method for adding a catalogue item to the basket.


#### catalogue.py

`Category`: Class - Category is a way of grouping items together by type.

`Size`: Class - Size is arbitrary and relevant to other matching items.

`Item`: Class - Items are things that a user would purchase.

`Catalogue`: Class - All the items and offers available in the shop.


#### offers.py

`OfferType`: Enum - Type of offer

`Offer`: Class - Offer to be applied to items