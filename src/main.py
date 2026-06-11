from fastapi import FastAPI
from .blogs.routes import router as blogs_router
from contextlib import asynccontextmanager
from .db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting...")
    await init_db()
    yield
    print(f"Server has stoppped")

current_version = "v1"

app = FastAPI(
    title="Micro Blogs",
    description="A Rest API for Micro blogging",
    version=current_version,
    lifespan=life_span
)

app.include_router(
    blogs_router,
    prefix=f"/api/{current_version}/blogs",
    tags=['blogs']
)


@app.get("/health")
async def health_check():
    return {
        "message": "I am Healthy..."
    }