"""
Central import hub. Import ALL SQLModel table models here, in dependency order.
This file is the single source of truth for Alembic and for app startup.

Rules:
  1. Models with no FK dependencies come first (User before Blog)
  2. Never import from this file back into domain model files
  3. Always import this module (not individual domain files) in alembic/env.py
"""
from src.users.models import User
from src.blogs.models import Blog

User.model_rebuild()
Blog.model_rebuild()


__all__ = ["User", "Blog"]
