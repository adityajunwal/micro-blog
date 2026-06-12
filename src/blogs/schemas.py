from pydantic import BaseModel
import uuid
from datetime import datetime, date
from typing import List

class Blog(BaseModel):
    uid: uuid.UUID
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

class BlogCreateModel(BaseModel):
    title: str
    content: str

