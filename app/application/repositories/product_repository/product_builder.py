from domain.entities.product import Product
from domain.models import Product as ProductModel
from domain.value_objects.money import Money
from domain.value_objects.quantity import Quantity


class ProductBuilder:
    def __init__(self, model: ProductModel) -> None:
        self._product = Product(
            name=model.name,
            quantity=Quantity(model.quantity),
            created_at=model.created_at,
            modified_at=model.modified_at,
            price=Money(model.price),
        )

    def builder(self) -> Product:
        return self._product
