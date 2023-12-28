from uuid import uuid4

from app.crud import crud_post
from app.models import Post
from app.schemas import PostCreate


async def generate_post(db) -> Post:
    post = Post(
        title=str(uuid4()),
        content=str(uuid4()),
        tags=[str(uuid4()), str(uuid4())],
    )
    return post


async def create_post(db) -> Post:
    post = await generate_post(db)
    post_schema = PostCreate(title=post.title, content=post.content, tags=post.tags)
    db_post = await crud_post.create_post(db, post_schema)
    return db_post
