from dataclasses import dataclass

import aiohttp


@dataclass
class NewsProxyService:
    base_url: str

    async def perform_request(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/news/tags.php?metro') as r:
                response = await r.text()
                return response
