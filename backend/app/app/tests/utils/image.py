import os

from app.core.config import settings


async def image_exists(name: str) -> bool:
    images = os.listdir(settings.UPLOAD_FOLDER)
    for image_name in images:
        if image_name == name:
            return True
    return False
