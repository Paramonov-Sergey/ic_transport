from typing import Optional, List

from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from schemas import NewsResponse
from services.news import NewsService

router = APIRouter(
    prefix='/news'
)


@router.get('/', response_model=List[NewsResponse], status_code=status.HTTP_200_OK)
async def get_news(
        day: Optional[int] = None,
        service: NewsService = Depends()
):
    """Получение новостей"""
    try:
        data = await service.get_list(day)
        return data
    except Exception as e:
        raise HTTPException(
            detail='News Not found',
            status_code=500
        )
