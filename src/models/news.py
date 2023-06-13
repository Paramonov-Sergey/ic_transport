from sqlalchemy import Column, Integer, String, DateTime,Text
from db.database import Base
from datetime import datetime


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    header = Column(Text, nullable=False)
    url = Column(String(length=2083), nullable=False)
    date = Column(DateTime, default=datetime.now())
