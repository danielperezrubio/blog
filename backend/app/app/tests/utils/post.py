from uuid import uuid4

from app.utils.admin import get_admin_user
from app.crud import crud_post
from app.models import Post
from app.schemas import PostCreate


async def generate_post(db) -> Post:
    admin = await get_admin_user(db)
    post = Post(
        title=str(uuid4()),
        content=str(uuid4()),
        tags=[str(uuid4()), str(uuid4())],
        owner_id=admin.id,
    )
    return post


async def create_post(db) -> Post:
    admin = await get_admin_user(db)
    post = await generate_post(db)
    post_schema = PostCreate(
        title=post.title, content=post.content, tags=post.tags, owner_id=post.owner_id
    )
    db_post = await crud_post.create_post(db, post_schema, admin.id)
    return db_post
