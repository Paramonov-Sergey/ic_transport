from fastapi import APIRouter
from .endpoints import news

api_router = APIRouter(
    prefix='/metro'
)

api_router.include_router(
    news.router,
    tags=['News']
)
