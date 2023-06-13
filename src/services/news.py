from typing import Optional

from crud.news import NewsCRUD
from schemas.news import NewsCreate
from services.base import BaseAppService
from services.news_proxy_service import NewsProxyService
from utils.parsers.news_parser import NewsParser


class NewsService(BaseAppService):

    async def get_list(self, day: Optional[int]):
        data = await NewsCRUD(db=self.db).get(day)
        return data

    async def load(self, base_url: str) -> None:
        service = NewsProxyService(base_url=base_url)
        response = await service.perform_request()
        parser = NewsParser(response)
        parser.parse()
        data = list(map(lambda news: NewsCreate(**news), parser.data))
        await NewsCRUD(db=self.db).bulk_create(data)
