from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from app.core.config import settings
from app.utils.token import create_user_activation_token, create_password_reset_token


async def create_config() -> ConnectionConfig:
    config = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_FROM=settings.MAIL_USERNAME,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_STARTTLS=settings.MAIL_STARTTLS,
        MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
        USE_CREDENTIALS=settings.USE_CREDENTIALS,
    )
    return config


async def send_email_activation_token(recipient: str, user_id: int) -> None:
    config = await create_config()
    token = await create_user_activation_token(user_id)
    html = f"""
            <h1>Click link bellow for activate your account</h1>
            <a href='{settings.WEBSITE_URL}/user/activate?token={token}'>
                Activate account</a>
    """
    fast_mail = FastMail(config)
    message = MessageSchema(
        subject="Account activation", recipients=[recipient], body=html, subtype="html"
    )
    await fast_mail.send_message(message)


async def send_password_reset_email(recipient: str, user_id) -> None:
    config = await create_config()
    token = await create_password_reset_token(user_id)
    html = f"""
        <h2>Click link bellow to change your password</h2>
        <a href='{settings.WEBSITE_URL}/user/change_password?token={token}'>
                Activate account</a>
    """
    message = MessageSchema(
        subject="Password reset", recipients=[recipient], body=html, subtype="html"
    )
    fast_mail = FastMail(config)
    await fast_mail.send_message(message)
