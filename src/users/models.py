from __future__ import annotations
from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
import uuid
from typing import List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from src.blogs.models import Blog


class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4()
        )
    )
    
    user_name: str = Field(index=True, nullable=False, unique=True)
    first_name: str = Field(nullable=False)
    middle_name: str | None = None
    last_name: str | None = None
    email: str = Field(index=True)
    password: str
    blogs: List["Blog"] | None = Relationship(back_populates="user")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now()))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now()))


