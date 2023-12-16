import pytest

from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.utils.token import create_password_reset_token, create_user_activation_token
from app.crud import crud_user

USER_ENDPOINT = f"/api/{settings.API_VERSION}/user"


@pytest.mark.asyncio
async def test_get_user(client: AsyncClient, db: AsyncSession, admin_headers: dict):
    response = await client.get(f"{USER_ENDPOINT}/me", headers=admin_headers)
    assert response.status_code == 200
    content = response.json()
    assert "id" in content
    assert content["is_active"] is True
    assert content["is_admin"] is True
    assert content["username"] == settings.FIRST_SUPERUSER_USERNAME


@pytest.mark.asyncio
async def test_reset_user_password(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    response = await client.get(
        f"{USER_ENDPOINT}/password?email={settings.FIRST_SUPERUSER_EMAIL}",
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_user_password(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    admin = await crud_user.get_user_by_email(db, settings.FIRST_SUPERUSER_EMAIL)
    token = await create_password_reset_token(admin.id)
    data = {"token": token, "password": "new_password"}
    response = await client.patch(f"{USER_ENDPOINT}/password", json=data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_user_password_invalid_token(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    admin = await crud_user.get_user_by_email(db, settings.FIRST_SUPERUSER_EMAIL)
    token = await create_user_activation_token(admin.id)
    data = {"token": token, "password": "new_password"}
    response = await client.patch(f"{USER_ENDPOINT}/password", json=data)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_activate_user(
    client: AsyncClient, db: AsyncSession, deactivated_admin_token: str
):
    admin = await crud_user.get_user_by_email(db, settings.FIRST_SUPERUSER_EMAIL)
    token = await create_user_activation_token(admin.id)
    response = await client.patch(f"{USER_ENDPOINT}/activate?token={token}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_activate_user_invalid_token(
    client: AsyncClient, db: AsyncSession, deactivated_admin_token: str
):
    admin = await crud_user.get_user_by_email(db, settings.FIRST_SUPERUSER_EMAIL)
    token = await create_password_reset_token(admin.id)
    response = await client.patch(f"{USER_ENDPOINT}/activate?token={token}")
    assert response.status_code == 401
