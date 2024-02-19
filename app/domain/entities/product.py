from dataclasses import dataclass

from domain.value_object import Money, Quantity


@dataclass
class Product:
    name: str
    quantity: Quantity
    price: Money
