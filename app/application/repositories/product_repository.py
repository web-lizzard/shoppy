from abc import abstractmethod, ABC
from domain.entities.product import Product
from domain.value_objects.money import Money
from domain.value_objects.quantity import Quantity
from domain.models import Product as ProductModel


class ProductBuilder:
    def __init__(self, model: ProductModel) -> None:
        self._product = Product(
            name=model.name,
            quantity=Quantity(model.quantity),
            created_at=model.created_at,
            modified_at=model.modified_at,
            price=Money.mint(model.price),
        )

    def builder(self) -> Product:
        return self._product


class ProductRepository(ABC):
    @abstractmethod
    async def get(self, name: str) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    async def list(self, skip: int = 0, limit: int = 100) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: str, product: Product) -> Product:
        raise NotImplementedError
