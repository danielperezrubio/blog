from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app import schemas, models
from app.utils.password import get_password_hash


async def create_user(db: AsyncSession, user: schemas.UserCreate, is_admin=False):
    db_user = models.User(
        user.username, user.email, get_password_hash(user.password), is_admin
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user(db: AsyncSession, id: int) -> models.User:
    return await db.get(models.User, id)


async def get_user_by_name(db: AsyncSession, username: str) -> models.User:
    statement = select(models.User).where(models.User.username == username)
    query = await db.execute(statement)
    user = query.scalar()
    return user


async def activate_user(db: AsyncSession, user_id: int) -> None:
    statement = (
        update(models.User).where(models.User.id == user_id).values(is_active=True)
    )
    await db.execute(statement)
    await db.commit()


async def get_user_by_email(db: AsyncSession, email: str) -> models.User:
    statement = select(models.User).where(models.User.email == email).limit(1)
    user = await db.scalar(statement)
    return user


async def update_user_password(db: AsyncSession, user_id: int, password: int) -> None:
    statement = (
        update(models.User)
        .where(models.User.id == user_id)
        .values(hashed_password=get_password_hash(password))
    )
    await db.execute(statement)
    await db.commit()
