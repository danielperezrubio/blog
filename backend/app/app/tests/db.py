from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.core.config import settings


class PostgresDatabaseNotFound(Exception):
    def __str__(self):
        return "POSTGRES_DB_TEST env variable not found!"


if not settings.POSTGRES_DB_TEST:
    raise PostgresDatabaseNotFound()

DATABASE_URL = settings.DATABASE_URL_TEST


def get_engine():
    engine = create_async_engine(DATABASE_URL)
    return engine


def get_session(engine):
    SessionLocal = async_sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )
    return SessionLocal


def get_engine_and_session():
    engine = get_engine()
    TestingSessionLocal = get_session(engine)
    return engine, TestingSessionLocal


async def override_get_db() -> AsyncSession:
    SessionLocal = get_engine_and_session()[1]
    try:
        db = SessionLocal()
        yield db
    finally:
        await db.close()
