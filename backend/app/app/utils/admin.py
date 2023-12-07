from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.config import settings
from app import schemas
from app.crud import crud_user
from app.models import User


async def create_first_superuser(db: AsyncSession):
    user = schemas.UserCreate(
        username=settings.FIRST_SUPERUSER_USERNAME,
        email=settings.FIRST_SUPERUSER_EMAIL,
        password=settings.FIRST_SUPERUSER_PASSWORD,
    )
    admin_user = await crud_user.create_user(db, user, is_admin=True)
    return admin_user


async def get_admin_user(db: AsyncSession) -> bool:
    statement = select(User).where(User.is_admin == True).limit(1)
    user = await db.scalar(statement)
    return user
