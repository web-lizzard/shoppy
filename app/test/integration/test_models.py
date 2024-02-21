from domain.models import Order, OrderedProduct, Product
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def test_create_product(session: AsyncSession):
    product = Product(name="test_item", quantity=2, price=10)

    session.add(product)

    await session.commit()
    await session.refresh(product)

    statement = select(Product).filter_by(name=product.name)
    db_product = await session.scalar(statement)

    assert db_product
