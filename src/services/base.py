from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_session


class BaseAppService:
    def __init__(
            self,
            db: AsyncSession = Depends(get_session),
    ):
        self.db = db
