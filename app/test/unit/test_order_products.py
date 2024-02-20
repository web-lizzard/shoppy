from dataclasses import replace

import pytest
from domain.entities.product import Product
from domain.value_objects.money import Money
from domain.value_objects.order_product import OrderedProduct, OrderedProducts
from domain.value_objects.quantity import Quantity


@pytest.fixture
def sample_ordered_products():
    product1 = OrderedProduct(
        quantity=Quantity(3),
        product=Product(name="Product 1", price=Money(500), quantity=Quantity(300)),
    )
    product2 = OrderedProduct(
        quantity=Quantity(2),
        product=Product(name="Product 2", price=Money(500), quantity=Quantity(300)),
    )
    return OrderedProducts([product1, product2])


def test_ordered_products_add_product_new(sample_ordered_products):
    new_product = OrderedProduct(
        quantity=Quantity(4),
        product=Product(name="New Product", price=Money(1000), quantity=Quantity(222)),
    )
    sample_ordered_products.add_product(new_product)
    assert len(sample_ordered_products) == 3


def test_ordered_products_add_product_existing(sample_ordered_products):
    existing_product = replace(sample_ordered_products[0], quantity=Quantity(2))
    sample_ordered_products.add_product(existing_product)
    assert sample_ordered_products[0].quantity == 5


def test_ordered_products_iter(sample_ordered_products):
    product_list = [product for product in sample_ordered_products]
    assert len(product_list) == 2
    assert isinstance(product_list[0], OrderedProduct)
