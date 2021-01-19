# -*- coding: utf-8 -*-
from shoppingcart.cart import ShoppingCart, ResourceNotPresent
import pytest


def test_add_item():
    """
    Test case to check add item functionality
    """
    cart = ShoppingCart()
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - €1.00"
    assert receipt[1] == "Total - 1 - €1.00"


def test_add_item_with_large_quantity():
    """
    Test case to check functionality to add item in large quantity
    """
    cart = ShoppingCart()
    cart.add_item("apple", 12)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 12 - €12.00"
    assert receipt[1] == "Total - 12 - €12.00"


def test_get_receipt_currencies():
    """
    Test case to check functionality of printing input currency in receipt
    """
    cart = ShoppingCart()
    cart.add_item("apple", 1)
    cart.add_item("kiwi", 1)

    receipt = cart.print_receipt("USD")

    assert receipt[0] == "apple - 1 - $1.19"
    assert receipt[1] == "kiwi - 1 - $3.57"
    assert receipt[2] == "Total - 2 - $4.76"


def test_add_different_items():
    """
    Test case to check functionality to add different items in the cart
    """
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 1 - €1.10"
    assert receipt[1] == "kiwi - 1 - €3.00"
    assert receipt[2] == "apple - 1 - €1.00"
    assert receipt[3] == "Total - 3 - €5.10"


def test_add_multiple_different_items():
    """
    Test case to check functionality to add different items in large quantity
    """
    cart = ShoppingCart()
    cart.add_item("banana", 2)
    cart.add_item("kiwi", 3)
    cart.add_item("apple", 4)

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 2 - €2.20"
    assert receipt[1] == "kiwi - 3 - €9.00"
    assert receipt[2] == "apple - 4 - €4.00"
    assert receipt[3] == "Total - 9 - €15.20"


def test_add_same_item():
    """
    Test case to check functionality to add same item multiple times
    """
    cart = ShoppingCart()
    cart.add_item("apple", 1)
    cart.add_item("banana", 2)
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 2 - €2.00"
    assert receipt[1] == "banana - 2 - €2.20"
    assert receipt[2] == "Total - 4 - €4.20"


def test_wrong_add_item():
    """
    Test case to check add item functionality
    """
    cart = ShoppingCart()
    with pytest.raises(ResourceNotPresent) as ex:

        cart.add_item("mango", 1)

        assert "Input Item does not exist." in str(ex.value)


def test_wrong_currency():
    """
    Test case to check different currency functionality
    """
    cart = ShoppingCart()
    cart.add_item("apple", 1)

    with pytest.raises(ResourceNotPresent) as ex:

        cart.print_receipt("Inr")

        assert "Input currency does not exist." in str(ex.value)
