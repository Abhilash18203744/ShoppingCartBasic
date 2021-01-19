import typing
import shoppingcart.abc as abc
import json
import os

# Path to price details and currency details json files
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), "data")
PRICE_DETAILS_PATH = os.path.join(DATA_DIR, "data.json")
CURRENCY_DETAILS_PATH = os.path.join(DATA_DIR, "currency.json")


class ShoppingCart(abc.ShoppingCart):
    """
    Class for shopping cart
    """

    def __init__(self):
        """
        Initialize shopping cart object with dictionary of item details in it.
        """
        self._items = dict()
        self.data = self._get_inventory_data()

    def _get_inventory_data(self) -> dict:
        """
        Get the inventory data including all information of available items.
        :return: data dictionary
        """
        try:
            with open(PRICE_DETAILS_PATH, 'r') as file:
                data = json.loads(file.read())

            return data

        except IOError as ex:
            print("Error : ", ex)

    def add_item(self, product_code: str, quantity: int):
        """
        Add items in the shopping cart
        :param product_code: item name
        :param quantity: total quantity of item added
        """
        if any(d['item_name'] == product_code for d in self.data['price_details']):
            if product_code not in self._items:
                self._items[product_code] = quantity
            else:
                q = self._items[product_code]
                self._items[product_code] = q + quantity
        else:
            raise ResourceNotPresent("Input Item does not exist.")

    def print_receipt(self, currency: str = "Euro") -> typing.List[str]:
        """
        Generate receipt for shopping cart
        :param currency: Requested currency in the receipt (default value is "euro")
        :return: list of items with total quantity and price
        """
        lines = []
        Total_price = 0
        Total_items = 0

        conversion_factor, sign = self._get_currency_details(currency)

        try:
            for item in self._items.items():
                price = self._get_product_price(item[0]) * item[1]
                price = price * conversion_factor

                Total_price += price
                Total_items += item[1]

                price_string = "{}{:.2f}".format(sign, round(price, 2))

                lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

            Total_price = "{}{:.2f}".format(sign, round(Total_price, 2))
            lines.append("Total - {} - {}".format(Total_items, Total_price))

            return lines

        except Exception as ex:
            print("Error : ", ex)

    def _get_product_price(self, product_code: str) -> float:
        """
        Get the price of input item from source
        :param product_code: item name
        :return: price of item
        """
        try:
            for item in self.data['price_details']:
                if product_code.lower() == item['item_name'].lower():
                    return item['item_price']

        except Exception as ex:
            print("Error : ", ex)

    def _get_currency_details(self, req_currency: str) -> list:
        """
        Get then currency sign and conversion factor
        :param req_currency: requested currency name
        :return: list of sign and conversion factor of input currency
        """
        try:
            with open(CURRENCY_DETAILS_PATH, encoding='utf-8') as file:
                data = json.loads(file.read())

        except IOError as ex:
            print("Error : ", ex)

        conversion_factor = sign = None
        for currency in data['currency_conversion']:
            if req_currency.lower() == currency['currency_name'].lower():
                conversion_factor, sign = currency['conversion_factor'], currency['sign']

        if conversion_factor and sign:
            return [conversion_factor, sign]
        raise ResourceNotPresent("Input currency does not exist.")


class ResourceNotPresent(Exception):
    """
    Class for raising exceptions on absence of requested resources
    """
    pass
