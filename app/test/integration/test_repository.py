import pytest

from application.repositories.product_repository.product_infrastracture import (
    SQLProductRepository,
)
from domain.entities.product import Product
from domain.models import Product as ProductModel
from domain.value_objects.quantity import Quantity
from domain.value_objects.money import Money
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(scope="session")
async def product_order(session: AsyncSession):
    product = ProductModel(name="test_item_fixture", quantity=2, price=10)

    session.add(product)

    await session.commit()


@pytest.fixture(scope="function")
async def product_repository(product_order, session_maker):
    repository = SQLProductRepository(session_factory=session_maker)

    yield repository


async def test_list_repository(product_repository):
    products = await product_repository.list()

    assert len(products)
    assert isinstance(products[0], Product)


async def test_get_product(product_repository: SQLProductRepository):
    product = await product_repository.get("test_item_fixture")

    assert product is not None
    assert isinstance(product, Product)


async def test_create_product(product_repository):
    product = Product(
        name="item-test-repository", quantity=Quantity(value=2), price=Money.mint(200)
    )

    await product_repository.create(product)

    saved_product = await product_repository.get(product.name)

    assert saved_product is not None
    assert isinstance(product, Product)


async def test_update_existence_product(product_repository):
    product = Product(
        name="test_item_fixture", quantity=Quantity(value=1), price=Money.mint(200)
    )

    updated_product = await product_repository.update(product)

    found_product = await product_repository.get(updated_product.name)

    assert updated_product.quantity == 1
    assert found_product == updated_product
