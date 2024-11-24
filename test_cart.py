import pytest

from Cart import ShoppingCart

def test_create_cart():
    assert ShoppingCart()

def test_add_items():
    test_cart = ShoppingCart()
    test_cart.add_item("lettuce")
    assert len(test_cart.get_items()) != 0