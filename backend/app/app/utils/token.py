from datetime import datetime, timedelta

from jose import jwt

from app.core.config import settings


class TokenType:
    ACTIVATION = "activation"
    PASSWORD_RESET = "password_reset"


async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    return token


async def create_user_activation_token(user_id: int):
    payload = {"user_id": user_id, "type": TokenType.ACTIVATION}
    return jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)


async def decode_token(token: str):
    payload = jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    return payload


async def create_password_reset_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "type": TokenType.PASSWORD_RESET,
        "exp": datetime.now() + timedelta(minutes=30),
    }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    return token
