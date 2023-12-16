import os

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.tests.utils.image import image_exists

IMAGE_ENDPOINT = f"/api/{settings.API_VERSION}/image"


@pytest.mark.asyncio
async def test_upload_file(client: AsyncClient, db: AsyncSession, admin_headers: dict):
    response = await client.post(
        IMAGE_ENDPOINT,
        files={
            "file": open(
                os.path.join(settings.APP_PATH, "tests", "images", "test_image.jpg"),
                "rb",
            )
        },
        headers=admin_headers,
    )
    assert response.status_code in [200, 201]
    content = response.json()
    name = content["image_name"]
    assert await image_exists(name) is True
