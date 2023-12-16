from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import crud_user
from app.core.config import settings
from app.utils.admin import create_first_superuser

TOKEN_ENDPOINT = f"/api/{settings.API_VERSION}/token"


async def get_admin_token(client: AsyncClient, db: AsyncSession, activate: bool = True):
    admin = await create_first_superuser(db)
    if activate:
        await crud_user.activate_user(db, admin.id)
    data = {
        "username": settings.FIRST_SUPERUSER_USERNAME,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    response = await client.post(TOKEN_ENDPOINT, data=data)
    token = response.json()["access_token"]
    return token


async def get_admin_headers(client: AsyncClient, db: AsyncSession):
    token = await get_admin_token(client, db)
    headers = {"Authorization": f"Bearer {token}"}
    return headers


async def get_deactivated_admin_token(client: AsyncClient, db: AsyncSession):
    token = await get_admin_token(client, db, activate=False)
    return token
