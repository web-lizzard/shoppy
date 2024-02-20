from dataclasses import replace

import pytest
from domain.entities.product import Product
from domain.value_objects.money import Money
from domain.value_objects.order_product import OrderedProduct
from domain.value_objects.quantity import Quantity


@pytest.fixture
def sample_ordered_product():
    return OrderedProduct(
        product=Product(name="Test Product", price=Money(100), quantity=Quantity(10)),
        quantity=Quantity(5),
    )


def test_ordered_product_add_quantity(sample_ordered_product):
    sample_ordered_product.add_quantity(Quantity(3))
    assert sample_ordered_product.quantity == 8


def test_ordered_product_equality_with_same_product(sample_ordered_product):
    same_product = replace(sample_ordered_product, quantity=Quantity(2))
    assert sample_ordered_product == same_product


def test_ordered_product_equality_with_different_product(sample_ordered_product):
    different_product = replace(
        sample_ordered_product,
        product=Product(
            name="Different Product", price=Money(200), quantity=Quantity(20)
        ),
    )
    assert sample_ordered_product != different_product
