from __future__ import annotations
from sqlmodel import SQLModel, Field, Column, Relationship
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.users.models import User
class Blog(SQLModel, table=True):
    __tablename__ = "blogs"

    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True, 
            default=uuid.uuid1()
        )
    )

    title: str
    content: str
    created_at: datetime = Field(sa_column=(Column(pg.TIMESTAMP, default=datetime.now())))
    updated_at: datetime = Field(sa_column=(Column(pg.TIMESTAMP, default=datetime.now())))
    user_id: uuid.UUID | None = Field(foreign_key="users.uid")
    user: "User" = Relationship(back_populates="blogs")
