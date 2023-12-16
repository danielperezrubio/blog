import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # General
    WEBSITE_URL: str
    API_VERSION: str = "v1"
    PROJECT_NAME: str = "Blog API"
    BACKEND_CORS_ORIGINS: str

    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str

    @property
    def DATABASE_URL(self) -> PostgresDsn:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}"
            + f":{self.POSTGRES_PASSWORD}"
            + f"@{self.POSTGRES_HOST}"
            + f"/{self.POSTGRES_DB}"
        )

    # Uploads
    APP_PATH: str = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    UPLOAD_FOLDER: str = os.path.join(APP_PATH, "media")

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 600

    # Admin
    FIRST_SUPERUSER_USERNAME: str
    FIRST_SUPERUSER_EMAIL: str
    FIRST_SUPERUSER_PASSWORD: str

    # Mail
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True

    # Tests
    UPLOAD_FOLDER_TEST: str = os.path.join(APP_PATH, "tests", "media")
    POSTGRES_DB_TEST: str = ""

    @property
    def DATABASE_URL_TEST(self) -> PostgresDsn:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}"
            + f":{self.POSTGRES_PASSWORD}"
            + f"@{self.POSTGRES_HOST}"
            + f"/{self.POSTGRES_DB_TEST}"
        )


settings = Settings()
