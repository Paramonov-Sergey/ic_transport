from datetime import datetime

from pydantic import BaseModel


class NewsResponse(BaseModel):
    header: str
    url: str
    date: datetime

    class Config:
        orm_mode = True


class NewsCreate(BaseModel):
    header: str
    url: str
