from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    tags: list[str]


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    owner_id: int
    published_at: datetime
    updated_at: datetime | None


class PostUpdate(PostBase):
    pass
