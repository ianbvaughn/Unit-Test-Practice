import pytest

from Cart import ShoppingCart

def test_create_cart():
    assert ShoppingCart(1)

def test_add_items():
    test_cart = ShoppingCart(1)
    test_cart.add_item("lettuce")
    assert test_cart.get_num_items() != 0

def test_exceed_cart_limit():
    test_cart = ShoppingCart(5)
    with pytest.raises(OverflowError):
        for i in range(6):
            test_cart.add_item(i)
        pass