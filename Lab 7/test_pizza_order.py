
from hypothesis import given, strategies as st
from pizza_order import toppings_price, pizza_inches, split_bill


# Test 1: Fuzz testing toppings_price()
@given(st.one_of(st.text(), st.none()))
def test_toppings_price_no_crash(s):
    result = toppings_price(s)
    assert result is None or isinstance(result, int)


# Test 2: Fuzz testing pizza_inches()
@given(st.one_of(st.text(), st.none()))
def test_pizza_inches_no_crash(s):
    result = pizza_inches(s)
    assert result is None or isinstance(result, int)


# Test 3: Fuzz testing split_bill()
@given(st.one_of(st.text(), st.none()))
def test_split_bill_no_crash(s):
    result = split_bill(s)
    assert result is None or isinstance(result, float)


# Test valid topping combinations
@given(st.lists(
    st.sampled_from(["cheese", "olives", "onion", "paneer"]),
    min_size=1
))
def test_valid_toppings(toppings):
    result = toppings_price(",".join(toppings))
    expected = sum(
        {"cheese": 40, "olives": 30, "onion": 20, "paneer": 50}[t]
        for t in toppings
    )
    assert result == expected


# Test valid pizza sizes
@given(st.sampled_from(["S", "M", "L", "s", "m", "l"]))
def test_valid_pizza_sizes(size):
    assert pizza_inches(size) in [8, 10, 12]
