from fastapi import APIRouter

from app.api.v1.endpoints import post, image, user, auth


api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(post.router, tags=["posts"])
api_router.include_router(image.router, tags=["images"])
api_router.include_router(user.router, tags=["users"])
