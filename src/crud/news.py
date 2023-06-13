from typing import Optional, List

from pydantic import BaseModel

from mixins.db_session_mixin import DBSessionMixin
from sqlalchemy import select

from models.news import News
from utils.get_date import get_date


class NewsCRUD(DBSessionMixin):

    async def get(self, day: Optional[int]):
        query = select(News)
        if day:
            date = get_date(day)
            query.filter(News.date >= date)
        result = await self.db.execute(query)
        objects = result.scalars().all()
        return objects

    async def bulk_create(self, data: List[BaseModel]):
        objects = [News(**obj.dict()) for obj in data]
        self.db.add_all(objects)
        await self.db.commit()
