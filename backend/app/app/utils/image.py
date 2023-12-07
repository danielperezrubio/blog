from uuid import uuid4
import os

from PIL import Image, UnidentifiedImageError

from app.core.config import settings


async def save_image(file):
    with Image.open(file.file) as image:
        image_name = str(uuid4()) + f".{image.format.lower()}"
        img_url = os.path.join(settings.UPLOAD_FOLDER, image_name)
        image.save(img_url)
        return image_name


async def is_valid_image(file) -> bool:
    try:
        with Image.open(file.file) as image:
            if image.format not in ["JPEG", "PNG"]:
                return False
            return True
    except UnidentifiedImageError:
        return False
