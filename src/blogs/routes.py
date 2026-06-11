from fastapi import APIRouter, status, HTTPException, Depends
from .schemas import Blog, BlogCreateModel
from fastapi.responses import JSONResponse
from .service import BlogService

from ..db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
import uuid

from typing import List

router = APIRouter()
service = BlogService()

@router.get("/", response_model=List[Blog])
async def get_all_blogs(
    session: AsyncSession = Depends(get_session)
):
    blogs = await service.get_all_blogs(session)
    return blogs

@router.get("/{blog_id}", response_model=Blog)
async def get_a_blog(
    blog_id: str,
    session: AsyncSession = Depends(get_session)
):
    blog = await service.get_blog(blog_id, session)
    if blog is None:
        raise HTTPException(detail="blog not found",status_code=status.HTTP_404_NOT_FOUND)

@router.post("/")
async def create_a_blog(
    blog: BlogCreateModel,
    session: AsyncSession = Depends(get_session)
):
    new_blog = await service.create_blog(blog, session)
    return new_blog

@router.patch("/{blog_id}")
async def update_a_blog(
    blog_id: str, 
    update_data: BlogCreateModel,
    session: AsyncSession = Depends(get_session)
):
    updated_blog = await service.update_blog(blog_id, update_data, session)

    if updated_blog is not None:
        return updated_blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="blog not found")

@router.delete("/{blog_id}")
async def delete_a_blog(
    blog_id: str,
    session: AsyncSession = Depends(get_session)
):
    blog_to_delete = await service.delete_blog(blog_id, session)

    if blog_to_delete is not None:
        return JSONResponse(
            content=f"Blog with id: {blog_id} DELETED succesfully",
            status_code=status.HTTP_204_NO_CONTENT
        )

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="blog not found"
        )
