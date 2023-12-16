from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Image


async def create_image(db: AsyncSession, image_name: str) -> Image:
    image = Image(image_name)
    db.add(image)
    await db.commit()
    await db.refresh(image)
    return image
