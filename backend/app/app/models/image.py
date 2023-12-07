from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    image_name = Column(String(50), nullable=False, unique=True)

    def __init__(self, image_name: str):
        self.image_name = image_name
