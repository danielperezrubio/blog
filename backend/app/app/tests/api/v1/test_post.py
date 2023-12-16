import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.tests.utils.post import generate_post, create_post

POST_ENDPOINT = f"/api/{settings.API_VERSION}/post"


@pytest.mark.asyncio
async def test_create_post(client: AsyncClient, db: AsyncSession, admin_headers: dict):
    post = await generate_post(db)
    data = {"title": post.title, "content": post.content, "tags": post.tags}
    response = await client.post(POST_ENDPOINT, json=data, headers=admin_headers)
    assert response.status_code == 201
    content = response.json()
    assert "id" in content
    assert content["title"] == post.title
    assert content["content"] == post.content
    assert content["tags"] == post.tags
    assert content["owner_id"] == post.owner_id


@pytest.mark.asyncio
async def test_create_post_invalid(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    data = {"title": "", "content": "", "tags": [""]}
    response = await client.post(POST_ENDPOINT, json=data, headers=admin_headers)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_get_post(client: AsyncClient, db: AsyncSession, admin_headers: dict):
    post = await create_post(db)
    response = await client.get(f"{POST_ENDPOINT}/{post.id}", headers=admin_headers)
    assert response.status_code == 200
    content = response.json()
    assert "id" in content
    assert content["title"] == post.title
    assert content["content"] == post.content
    assert content["tags"] == post.tags
    assert content["owner_id"] == post.owner_id


@pytest.mark.asyncio
async def test_get_post_not_found(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    post = await create_post(db)
    response = await client.get(f"{POST_ENDPOINT}/{post.id + 1}", headers=admin_headers)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_posts(client: AsyncClient, db: AsyncSession, admin_headers: dict):
    post1 = await create_post(db)
    post2 = await create_post(db)
    post3 = await create_post(db)
    params = "limit=2&offset=1"
    response = await client.get(f"{POST_ENDPOINT}?{params}", headers=admin_headers)
    assert response.status_code == 200
    posts = response.json()
    posts_ids = [post["id"] for post in posts]
    assert post3.id not in posts_ids
    assert post2.id in posts_ids
    assert post1.id in posts_ids


@pytest.mark.asyncio
async def test_get_posts_without_content(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    for i in range(3):
        await create_post(db)
    params = "limit=3&offset=0&send_content=false"
    response = await client.get(f"{POST_ENDPOINT}?{params}", headers=admin_headers)
    assert response.status_code == 200
    posts = response.json()
    for post in posts:
        assert post["content"] == ""


@pytest.mark.asyncio
async def test_update_post(client: AsyncClient, db: AsyncSession, admin_headers: dict):
    post = await create_post(db)
    new_post = await generate_post(db)
    data = {"title": new_post.title, "content": new_post.content, "tags": new_post.tags}
    response = await client.put(
        f"{POST_ENDPOINT}/{post.id}", json=data, headers=admin_headers
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == new_post.title
    assert content["content"] == new_post.content
    assert content["tags"] == new_post.tags


@pytest.mark.asyncio
async def test_update_post_not_found(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    post = await create_post(db)
    new_post = await generate_post(db)
    data = {"title": new_post.title, "content": new_post.content, "tags": new_post.tags}
    response = await client.put(
        f"{POST_ENDPOINT}/{post.id + 1}", json=data, headers=admin_headers
    )
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_post(client: AsyncClient, db: AsyncSession, admin_headers: dict):
    post = await create_post(db)
    response = await client.delete(f"{POST_ENDPOINT}/{post.id}", headers=admin_headers)
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_post_not_found(
    client: AsyncClient, db: AsyncSession, admin_headers: dict
):
    post = await create_post(db)
    response = await client.delete(
        f"{POST_ENDPOINT}/{post.id + 1}", headers=admin_headers
    )
    assert response.status_code == 404
