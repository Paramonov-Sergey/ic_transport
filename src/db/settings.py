from pydantic import BaseSettings, Field


class PostgreSQLDBSettings(BaseSettings):
    """Настройки БД"""
    DATABASE_URL: str = ""
