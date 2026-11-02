
import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# PIZZA PRICE - BRANCH TESTS

def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra_large", 2, False)

def test_valid_size():
    assert pizza_price("small", 1, False) == 240

def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("small", -1, False)

def test_valid_toppings():
    assert pizza_price("medium", 2, False) == 430

def test_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680

def test_cheese_burst_small():
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)

def test_cheese_burst_medium():
    assert pizza_price("medium", 0, True) == 450


# ORDER DISCOUNT - BRANCH TESTS

def test_order_below_300():
    assert order_discount(200, "monday", False) == 0

def test_tuesday_discount():
    assert order_discount(400, "tuesday", False) == 200

def test_weekend_discount():
    assert order_discount(400, "saturday", False) == 0

def test_weekday_discount():
    assert order_discount(400, "monday", False) == 40

def test_student_discount():
    assert order_discount(400, "monday", True) == 90


# DELIVERY STATUS - BRANCH TESTS

def test_distance_above_10():
    assert delivery_status(20, 12) == "not deliverable"

def test_distance_within_limit():
    assert delivery_status(20, 10) == "on time"

def test_exactly_30_minutes():
    assert delivery_status(30, 5) == "on time"

def test_exactly_45_minutes():
    assert delivery_status(45, 5) == "late"

def test_above_45_minutes():
    assert delivery_status(46, 5) == "free pizza"
