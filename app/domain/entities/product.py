from dataclasses import dataclass, field
from datetime import datetime

from domain.exceptions import OutOfStock
from domain.value_objects.money import Money
from domain.value_objects.quantity import Quantity


@dataclass
class Product:
    name: str
    quantity: Quantity
    price: Money
    created_at: datetime = field(default_factory=datetime.now)
    modified_at: datetime = field(default_factory=datetime.now)

    def add_quantity(self, quantity: Quantity):
        self.quantity = self.quantity + quantity

    def decrement_quantity(self, quantity: Quantity):
        try:
            self.quantity = self.quantity - quantity
        except ValueError:
            raise OutOfStock(f"Not sufficient amount of {self.name}")
