from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base


class EntryBase(BaseModel):
    title: str
    bookmark: Optional[str] = None
    media_type: Optional[str] = None
    genre: Optional[str] = None
    content_url: Optional[str] = None


class Entry(EntryBase):
    id: int
    thumbnail_url: Optional[str] = None

    model_config = {
        "from_attributes": True
    }

class EntryDB(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    bookmark: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    media_type: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    genre: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    content_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    thumbnail_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)