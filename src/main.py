import uvicorn
from fastapi import FastAPI
from api.api_router import api_router
from core.config import settings
from fastapi_utils.tasks import repeat_every

from db.database import async_session, init_db
from services.news import NewsService

app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(api_router)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.on_event('startup')
@repeat_every(seconds=60*10, wait_first=True)
async def load_news():
    async with async_session() as session:
        await NewsService(db=session).load(base_url=settings.NEWS_URI)


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        port=settings.server_port,
    )

