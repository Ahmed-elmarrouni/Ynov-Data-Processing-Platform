import pytest
from src.validation.schema import Order


def test_valid_order():
    order = Order(product="Laptop", quantity=2, price=1000.0, country="USA")
    assert order.product == "Laptop"


def test_invalid_order_price():
    with pytest.raises(ValueError):
        Order(product="Mouse", quantity=1, price=-10.0, country="USA")


# def test_invalid_country():
#     with pytest.raises(ValueError):
#         Order(product="Keyboard", quantity=1, price=50.0, country="Morocco")
