import os

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
        TEMPLATE_FOLDER=os.path.join(settings.APP_PATH, "utils", "email_templates"),
    )
    return config


async def send_email_activation_token(recipient: str, user_id: int) -> None:
    config = await create_config()
    token = await create_user_activation_token(user_id)
    fast_mail = FastMail(config)
    body = {"url": settings.WEBSITE_URL, "token": token}
    message = MessageSchema(
        subject="Account activation",
        recipients=[recipient],
        template_body=body,
        subtype="html",
        attachments=[
            {
                "file": os.path.join(
                    settings.APP_PATH, "utils", "email_templates", "blog-logo.png"
                ),
                "headers": {
                    "Content-ID": "blog-logo",
                    "Content-Disposition": 'inline; filename="blog-logo.png"',
                },
                "mime_type": "image",
                "mime_subtype": "png",
            }
        ],
    )
    await fast_mail.send_message(message, template_name="activate_user.html")


async def send_password_reset_email(recipient: str, user_id) -> None:
    config = await create_config()
    token = await create_password_reset_token(user_id)
    body = {"url": settings.WEBSITE_URL, "token": token}
    message = MessageSchema(
        subject="Password reset",
        recipients=[recipient],
        template_body=body,
        subtype="html",
        attachments=[
            {
                "file": os.path.join(
                    settings.APP_PATH, "utils", "email_templates", "blog-logo.png"
                ),
                "headers": {
                    "Content-ID": "blog-logo",
                    "Content-Disposition": 'inline; filename="blog-logo.png"',
                },
                "mime_type": "image",
                "mime_subtype": "png",
            }
        ],
    )
    fast_mail = FastMail(config)
    await fast_mail.send_message(message, template_name="reset_password.html")
