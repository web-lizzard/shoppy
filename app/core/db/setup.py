from config import settings
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine(settings.database.url, echo=settings.database.echo_sql)
DEFAULT_SESSION_FACTORY = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
TestingSessionLocal = async_sessionmaker(
    bind=create_async_engine(TEST_DATABASE_URL), expire_on_commit=False
)
