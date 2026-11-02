
import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# PIZZA PRICE TESTS

def test_plain_medium():
    assert pizza_price("medium", 0, False) == 350

def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra_large", 2, False)

def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("small", -1, False)

def test_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680

def test_cheese_burst_small():
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)

def test_cheese_burst_medium():
    assert pizza_price("medium", 2, True) == 530


# ORDER DISCOUNT TESTS

def test_order_below_300():
    assert order_discount(200, "monday", True) == 0

def test_tuesday_student():
    assert order_discount(400, "tuesday", True) == 250

def test_weekend_discount():
    assert order_discount(400, "sunday", False) == 0

def test_normal_weekday():
    assert order_discount(400, "monday", True) == 90


# DELIVERY STATUS TESTS

def test_not_deliverable():
    assert delivery_status(20, 12) == "not deliverable"

def test_on_time():
    assert delivery_status(20, 3) == "on time"

def test_late():
    assert delivery_status(40, 5) == "late"

def test_free_pizza():
    assert delivery_status(50, 5) == "free pizza"
