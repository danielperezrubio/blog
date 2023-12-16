from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app import schemas, models
from app.crud import crud_post
from app.api.deps import get_current_active_user
from app.utils.bleach import clean_html

router = APIRouter()


async def common_validations(post):
    if not post.title:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="title is required")
    if not post.content:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="content is required")
    if not post.tags:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="tags is required")


@router.post("/post", status_code=201)
async def create_post(
    db: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[models.User, Depends(get_current_active_user)],
    post: schemas.PostCreate,
) -> schemas.PostResponse:
    await common_validations(post)
    cleaned_post = await clean_html(post.content)
    post.content = cleaned_post
    db_post = await crud_post.create_post(db, post, current_user.id)
    return db_post


@router.get("/post/{id}")
async def get_post(
    db: Annotated[AsyncSession, Depends(get_db)], id: int
) -> schemas.PostResponse:
    post = await crud_post.get_post(db, id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="post not found")
    return post


@router.get("/post")
async def get_posts(
    db: Annotated[AsyncSession, Depends(get_db)],
    limit: Annotated[int, Query(le=20)] = 10,
    offset: int = 0,
    send_content: bool = True,
    filter_word: str | None = None,
) -> list[schemas.PostResponse]:
    posts = await crud_post.get_posts(db, limit, offset, filter_word)
    if send_content is not True:
        for post in posts:
            post.content = ""
    return posts


@router.put("/post/{id}")
async def update_post(
    db: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[models.User, Depends(get_current_active_user)],
    id: int,
    post: schemas.PostUpdate,
) -> schemas.PostResponse:
    await common_validations(post)
    db_post = await crud_post.get_post(db, id)
    if not db_post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="post not found")
    if db_post.owner_id != current_user.id:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="the current user is not the owner of the post",
        )
    post.content = await clean_html(post.content)
    db_post = await crud_post.update_post(db, db_post, post)
    return db_post


@router.delete("/post/{id}", status_code=204)
async def delete_post(
    db: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[models.User, Depends(get_current_active_user)],
    id: int,
):
    post = await crud_post.get_post(db, id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="the current user is not the owner of the post",
        )
    await crud_post.delete_post(db, post)
    return {}
