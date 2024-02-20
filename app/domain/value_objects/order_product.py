from dataclasses import dataclass
from functools import reduce

from domain.entities.product import Product
from domain.value_objects.money import Money
from domain.value_objects.quantity import Quantity


@dataclass
class OrderedProduct:
    quantity: Quantity
    product: Product

    def add_quantity(self, quantity: Quantity):
        self.quantity += quantity

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, OrderedProduct):
            return __value.product.name == self.product.name

        raise TypeError("Not supported value to compare")


@dataclass
class OrderedProducts:
    _products: list[OrderedProduct]

    def __init__(self, products: list[OrderedProduct] | None = None):
        self._products = products or []

    @property
    def total_price(self) -> Money:
        return reduce(
            lambda x, y: x + Money.mint(y.quantity.value * y.product.price.amount),
            self._products,
            Money.mint(0),
        )

    def add_product(self, product_to_add: OrderedProduct):
        product = self._find_product(product=product_to_add)
        if product is None:
            return self._products.append(product_to_add)

        product.add_quantity(product_to_add.quantity)

    def remove_product(self, product: OrderedProduct):
        self._products.remove(product)

    def __len__(self):
        return len(self._products)

    def __getitem__(self, object):
        if isinstance(object, int):
            return self._products[object]

        raise TypeError

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._products):
            current_product = self._products[self.index]
            self.index += 1
            return current_product
        raise StopIteration

    def _find_product(self, product: OrderedProduct) -> None | OrderedProduct:
        for product_in_collection in self._products:
            if product == product_in_collection:
                return product_in_collection
        return None
