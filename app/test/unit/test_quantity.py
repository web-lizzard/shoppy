import pytest
from domain.value_object import Quantity


def test_creation():
    quantity = Quantity(5)
    assert quantity.value == 5


def test_negative_creation():
    with pytest.raises(ValueError):
        Quantity(-5)


def test_addition():
    quantity1 = Quantity(5)
    quantity2 = Quantity(3)
    result = quantity1 + quantity2
    assert result.value == 8


def test_multiplication():
    quantity = Quantity(5)
    result = quantity * 2
    assert result.value == 10


def test_division():
    quantity = Quantity(10)
    result = quantity / 2
    assert result.value == 5
