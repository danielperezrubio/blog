import os

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.main import app
from app.db.database import get_db
from app.core.config import settings
from app.tests.db import override_get_db, get_engine_and_session
from app.db.database import Base
from app.tests.utils.user import get_admin_headers, get_deactivated_admin_token

# Replace real database dependency for tests
app.dependency_overrides[get_db] = override_get_db

# Replace real upload folder for tests)
settings.UPLOAD_FOLDER = settings.UPLOAD_FOLDER_TEST


async def clean_images():
    media_folder = settings.UPLOAD_FOLDER
    for filename in os.listdir(media_folder):
        if filename != ".git-keep":
            file_path = os.path.join(media_folder, filename)
            os.remove(file_path)


@pytest_asyncio.fixture
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture
async def db() -> AsyncSession:
    async_engine, SessionLocal = get_engine_and_session()
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    async with SessionLocal() as session:
        yield session
        await clean_images()


@pytest_asyncio.fixture
async def admin_headers(client: AsyncClient, db: AsyncSession) -> dict:
    headers = await get_admin_headers(client, db)
    return headers


@pytest_asyncio.fixture
async def deactivated_admin_token(client: AsyncClient, db: AsyncSession) -> dict:
    token = await get_deactivated_admin_token(client, db)
    return token
