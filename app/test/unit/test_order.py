from domain.entities import order as order_domain
from domain.entities import product
from domain.value_objects.money import Money
from domain.value_objects.quantity import Quantity


def get_order() -> order_domain.Order:
    return order_domain.Order()


def get_product() -> product.Product:
    return product.Product(
        name="test-name", quantity=Quantity(3), price=Money.mint(1000)
    )


def test_order_adding_order_info():
    order = get_order()
    order_info = order_domain.OrderInfo(address="example", email="test@email.com")
    order.set_order_info(order_info=order_info)

    assert order_info is order.order_info


def test_order_adding_ordered_product():
    product = get_product()
    product_in_cart = order_domain.OrderedProduct(quantity=Quantity(1), product=product)
    order = get_order()

    order.add_product_to_order(product_to_add=product_in_cart)

    assert product_in_cart in order.ordered_products


def test_adding_same_product_update_quantity():
    product = get_product()
    order = get_order()
    product_in_cart = order_domain.OrderedProduct(quantity=Quantity(1), product=product)
    product_in_cart_2 = order_domain.OrderedProduct(
        quantity=Quantity(1), product=product
    )

    order.add_product_to_order(product_in_cart)
    order.add_product_to_order(product_in_cart_2)

    assert len(order.ordered_products) == 1
    assert order.ordered_products[0].quantity == 2


def test_ready_to_order():
    order = get_order()
    product = get_product()
    product_in_cart = order_domain.OrderedProduct(quantity=Quantity(1), product=product)
    order_info = order_domain.OrderInfo(address="address", email="r@com.pl")

    order.add_product_to_order(product_to_add=product_in_cart)
    order.set_order_info(order_info)

    assert order.ready_to_order is True
