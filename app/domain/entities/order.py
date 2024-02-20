from dataclasses import dataclass, field

from domain.value_objects.order_product import OrderedProduct, OrderedProducts


@dataclass(frozen=True)
class OrderInfo:
    address: str
    email: str


@dataclass
class Order:
    ordered_products: OrderedProducts = field(default_factory=lambda: OrderedProducts())
    order_info: OrderInfo | None = None

    def set_order_info(self, order_info: OrderInfo):
        self.order_info = order_info

    def add_product_to_order(self, product_to_add: OrderedProduct):
        self.ordered_products.add_product(product_to_add)
