import aioredis
from app.config import settings

if settings.MODE == "DEV":
    redis_url = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"
else:
    redis_url = settings.INTERNAL_REDIS_URL

class AsyncRedis:
    redis_pool = None
    
    async def __aenter__(self):
        self.redis_pool = aioredis.from_url(redis_url, encoding="utf8", decode_responses=True)
        return self.redis_pool
        
    async def __aexit__(self, *args):
        await self.redis_pool.close()
        
        