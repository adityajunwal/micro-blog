from sqlmodel.ext.asyncio.session import AsyncSession
from .models import Blog
from sqlmodel import select, desc
from datetime import datetime
from .schemas import BlogCreateModel

class BlogService:
    async def get_all_blogs(self, session: AsyncSession):
        statement = select(Blog).order_by(desc(Blog.created_at))
        result = await session.exec(statement)

        return result.all()
    
    async def get_blog(self, blog_id: str, session: AsyncSession):
        statement = select(Blog).where(Blog.uid == blog_id)
        result = await session.exec(statement)

        return result.first()

    async def create_blog(self, blog_data: BlogCreateModel, session: AsyncSession):
        blog_data_dict = blog_data.model_dump()
        new_blog = Blog(
            **blog_data_dict
        )

        session.add(new_blog)
        await session.commit()

        return new_blog
    
    async def update_blog(self, blog_id: str,  updated_blog_data: BlogCreateModel, session: AsyncSession):
        blog_to_update = await self.get_blog(blog_id, session)

        if blog_to_update is not None:
            update_data_dict = updated_blog_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(blog_to_update, k, v)

                await session.commit()
                return blog_to_update
        
        else:
            return None

    async def delete_blog(self, blog_id: str, session: AsyncSession):
        blog_to_delete = self.get_blog(blog_id)

        if blog_to_delete is not None:
            await session.delete(blog_to_delete)
            await session.commit()

            return blog_to_delete
        else:
            return None


