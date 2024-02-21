from abc import abstractmethod, ABC
from typing import Callable
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from domain.entities.product import Product
from domain.value_objects.money import Money
from domain.value_objects.quantity import Quantity
from domain.models import Product as ProductModel
from sqlalchemy import select
from datetime import datetime
from dataclasses import asdict


class ProductNotFound(Exception):
    pass


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
    async def create(self, product: Product):
        raise NotImplementedError

    @abstractmethod
    async def update(self, id: str, product: Product) -> Product:
        raise NotImplementedError


class SQLProductRepository(ProductRepository):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def list(self, skip: int = 0, limit: int = 100) -> list[Product]:
        async with self._session_factory() as session:
            statement = select(ProductModel).offset(skip).limit(limit)
            db_products = await session.scalars(statement)

            return [ProductBuilder(product).builder() for product in db_products]

    async def get(self, name: str) -> Product | None:
        async with self._session_factory() as session:
            statement = select(ProductModel).filter_by(name=name)
            db_product = await session.scalar(statement)
            return ProductBuilder(db_product).builder() if db_product else None

    async def create(self, product: Product):
        async with self._session_factory() as session:
            model = ProductModel(
                name=product.name,
                quantity=product.quantity.value,
                price=product.price.amount,
                created_at=product.created_at,
                modified_at=product.modified_at,
            )
            session.add(model)

            await session.commit()
            await session.refresh(model)

    async def update(self, product: Product) -> Product:
        async with self._session_factory() as session:
            statement = select(ProductModel).filter_by(name=product.name)
            db_product = await session.scalar(statement)

            if db_product is None:
                raise ValueError

            for key, value in asdict(product).items():
                if isinstance(value, dict):
                    continue
                setattr(db_product, key, value)

            db_product.quantity = product.quantity.value
            db_product.price = product.price.amount
            db_product.modified_at = datetime.now()

            await session.commit()
            await session.refresh(db_product)

            return ProductBuilder(db_product).builder()
