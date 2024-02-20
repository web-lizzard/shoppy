import pytest
from core.db.models import Base
from domain.models import Order, Product
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(autouse=True, scope="session")
async def engine():
    engine = create_async_engine(TEST_DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield engine


@pytest.fixture(autouse=True, scope="session")
async def session_maker(engine):
    yield async_sessionmaker(engine, autoflush=False, class_=AsyncSession)


@pytest.fixture(autouse=True)
async def session(session_maker):
    yield session_maker()


@pytest.fixture(scope="function")
async def product_order(session: AsyncSession):
    order = Order()
    product = Product(name="test_item", quantity=2, price=10)

    session.add_all([product, order])

    await session.commit()
    yield


@pytest.fixture(autouse=True, scope="function")
async def drop_table(engine: AsyncEngine):
    yield
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.drop_all)
