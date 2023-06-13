from pathlib import Path
from db.settings import PostgreSQLDBSettings

configs = [PostgreSQLDBSettings]
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(*configs):
    # server settings
    server_host: str = "127.0.0.1"
    server_port: int = 7040
    # application settings
    PROJECT_NAME: str = "IcTransport"
    DEBUG: bool = True
    NEWS_URI: str = ''
    cors_allowed_origins = ['*']


settings = Settings(
    _env_file=f'{BASE_DIR.parent}/.env',
    _env_file_encoding='utf-8'
)
