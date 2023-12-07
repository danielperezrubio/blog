from sqlalchemy import Column, Integer, String, Boolean

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    def __init__(self, username, email, hashed_password, is_admin=False):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_admin = is_admin
