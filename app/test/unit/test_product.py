import pytest
from domain.entities.product import Product
from domain.exceptions import OutOfStock
from domain.value_object import Money, Quantity


def get_product() -> Product:
    money = Money.mint(amount=2000)
    quantity = Quantity(value=2)
    return Product(name="product", price=money, quantity=quantity)


def test_add_quantity_to_product():
    product = get_product()
    new_quantity = Quantity(value=3)

    product.add_quantity(quantity=new_quantity)

    assert product.quantity == 5


def test_subtract_quantity():
    product = get_product()

    new_quantity = Quantity(value=1)

    product.decrement_quantity(quantity=new_quantity)

    assert product.quantity == 1


def test_subtract_too_many_quantity_raises_out_of_stock():
    product = get_product()
    quantity = Quantity(value=2137)

    with pytest.raises(OutOfStock):
        product.decrement_quantity(quantity=quantity)
