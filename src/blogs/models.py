from sqlmodel import SQLModel, Field, Column, Relationship
from typing import Optional
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

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
    update_at: datetime = Field(sa_column=(Column(pg.TIMESTAMP, default=datetime.now())))
