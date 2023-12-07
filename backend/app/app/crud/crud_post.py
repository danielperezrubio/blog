from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from app.models import Post
from app import schemas


async def create_post(
    db: AsyncSession, post: schemas.PostCreate, owner_id: int
) -> Post:
    db_post = Post(
        title=post.title, content=post.content, tags=post.tags, owner_id=owner_id
    )
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post


async def get_post(db: AsyncSession, id: int) -> Post:
    post = await db.get(Post, id)
    return post


async def get_posts(
    db: AsyncSession, limit: int, offset: int, filter_word: str | None = None
) -> list[Post]:
    statement = select(Post).order_by(-Post.id).limit(limit).offset(offset)
    if filter_word:
        statement = statement.where(
            or_(
                Post.title.icontains(filter_word),
                Post.tags.contains([filter_word]),
            )
        )
    posts = await db.scalars(statement)
    return [post for post in posts]


async def update_post(db: AsyncSession, db_post: Post, post: schemas.PostUpdate):
    db_post.title = post.title
    db_post.content = post.content
    db_post.tags = post.tags
    db_post.updated_at = datetime.now()
    db.add(db_post)
    await db.commit()
    await db.refresh(db_post)
    return db_post


async def delete_post(db: AsyncSession, post: Post):
    await db.delete(post)
    await db.commit()
