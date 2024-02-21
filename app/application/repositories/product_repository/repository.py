from abc import ABC, abstractmethod

from domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    async def get(self, name: str) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    async def list(self, skip: int = 0, limit: int = 100) -> list[Product]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, product: Product):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: str, product: Product) -> Product:
        raise NotImplementedError
