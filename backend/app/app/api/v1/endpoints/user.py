from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError
from pydantic import EmailStr

from app.db.database import get_db
from app.utils.token import (
    decode_token,
    TokenType,
)
from app.utils.mail import send_password_reset_email
from app.crud import crud_user
from app.models import User
from app.api.deps import get_current_active_user
from app.schemas import UserResponse, UserPasswordUpdate


router = APIRouter()


@router.get("/user/me")
async def get_user(
    db: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_active_user)],
) -> UserResponse:
    """
    Get current user.
    """
    return current_user


@router.get("/user/password")
async def reset_user_password(
    db: Annotated[AsyncSession, Depends(get_db)],
    email: EmailStr,
    background_tasks: BackgroundTasks,
):
    """
    Send an email to the user with the reset password link.
    """
    user = await crud_user.get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="the provided email is not associated with any account.",
        )
    background_tasks.add_task(send_password_reset_email, user.email, user.id)
    return {"message": "Check you email to proceed"}


@router.patch("/user/password")
async def update_user_password(
    db: Annotated[AsyncSession, Depends(get_db)], data: UserPasswordUpdate
):
    """
    Update user password.
    """
    invalid_token_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
    )
    try:
        payload = await decode_token(data.token)
        if not payload["type"] == TokenType.PASSWORD_RESET:
            raise invalid_token_exception
    except JWTError:
        raise invalid_token_exception
    await crud_user.update_user_password(db, payload.get("user_id"), data.password)
    return {"message": "Password has been changed"}


@router.patch("/user/activate")
async def activate_user(db: Annotated[AsyncSession, Depends(get_db)], token: str):
    """
    Activate an user.
    """
    invalid_token_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
    )
    try:
        payload = await decode_token(token)
        if not payload["type"] == TokenType.ACTIVATION:
            raise invalid_token_exception
    except JWTError:
        raise invalid_token_exception
    await crud_user.activate_user(db, payload["user_id"])
    return {"message": "The user account has been activated!"}
