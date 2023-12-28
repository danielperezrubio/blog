from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import ARRAY, VARCHAR
from app.db.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    tags = Column(ARRAY(VARCHAR), nullable=False)
    published_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime)

    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags
