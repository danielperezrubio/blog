from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.v1.api import api_router
from app.core.config import settings
from app.db.database import SessionLocal
from app.utils.admin import create_first_superuser, get_admin_user
from app.utils.mail import send_email_activation_token

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    db: AsyncSession = SessionLocal()
    admin_user = await get_admin_user(db)
    if not admin_user:
        admin_user = await create_first_superuser(db)
    if not admin_user.is_active:
        await send_email_activation_token(admin_user.email, admin_user.id)
    await db.close()


app.include_router(api_router, prefix=f"/api/{settings.API_VERSION}")
app.mount("/static/", StaticFiles(directory=settings.UPLOAD_FOLDER), name="static")
