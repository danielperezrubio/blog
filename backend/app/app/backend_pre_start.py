import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import SessionLocal
from app.utils.admin import create_first_superuser, get_admin_user
from app.utils.mail import send_email_activation_token


async def create_admin_if_not_exist():
    db: AsyncSession = SessionLocal()
    admin_user = await get_admin_user(db)
    if not admin_user:
        admin_user = await create_first_superuser(db)
    if not admin_user.is_active:
        await send_email_activation_token(admin_user.email, admin_user.id)
    await db.close()


if __name__ == "__main__":
    asyncio.run(create_admin_if_not_exist())
