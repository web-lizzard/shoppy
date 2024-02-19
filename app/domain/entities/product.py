from dataclasses import dataclass

from domain.exceptions import OutOfStock
from domain.value_object import Money, Quantity


@dataclass
class Product:
    name: str
    quantity: Quantity
    price: Money

    def add_quantity(self, quantity: Quantity):
        self.quantity = self.quantity + quantity

    def decrement_quantity(self, quantity: Quantity):
        try:
            self.quantity = self.quantity - quantity
        except ValueError:
            raise OutOfStock(f"Not sufficient amount of {self.name}")
