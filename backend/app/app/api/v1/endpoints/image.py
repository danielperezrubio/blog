from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.crud import crud_image
from app.models import User
from app.api.deps import get_current_active_user
from app.utils.image import save_image, is_valid_image

router = APIRouter()


@router.post("/image")
async def upload_file(
    db: Annotated[AsyncSession, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_active_user)],
    file: UploadFile,
):
    if not await is_valid_image(file):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid image")
    image_name = await save_image(file)
    image = await crud_image.create_image(db, image_name)
    return {"filename": image}
