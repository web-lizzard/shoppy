from dataclasses import dataclass, field
from datetime import datetime, timedelta

from domain.value_objects.order_product import OrderedProduct, OrderedProducts

ORDER_EXPIRATION_TIME_IN_MINUTES = 30


@dataclass(frozen=True)
class OrderInfo:
    address: str
    email: str


@dataclass
class Order:
    ordered_products: OrderedProducts = field(default_factory=lambda: OrderedProducts())
    order_info: OrderInfo | None = None
    start_at: datetime = field(default_factory=datetime.now)
    expired_at: datetime = field(
        default_factory=lambda: datetime.now()
        + timedelta(minutes=ORDER_EXPIRATION_TIME_IN_MINUTES)
    )

    @property
    def total_cost(self):
        return self.ordered_products.total_price

    @property
    def is_expired(self) -> bool:
        return self.expired_at < datetime.now()

    @property
    def ready_to_order(self) -> bool:
        return bool(
            len(self.ordered_products) and self.order_info and not self.is_expired
        )

    def set_order_info(self, order_info: OrderInfo):
        self.order_info = order_info

    def add_product_to_order(self, product_to_add: OrderedProduct):
        self.ordered_products.add_product(product_to_add)

    def remove_product_from_order(self, product: OrderedProduct):
        self.ordered_products.remove_product(product)
