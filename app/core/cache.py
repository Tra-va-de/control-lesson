import logging

from redis import asyncio as redis

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from core.config import settings


async def init_cache():
    try:
        redis_client = await redis.from_url(settings.REDIS_URL, encoding="utf8", decode_responses=True)
        FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
        logging.info("Cache initialized successfully")
        print("КЭШ подключен")
    except Exception as e:
        logging.error(f"Failed to initialize cache: {str(e)}")
        print("Ошибка подключения КЭШ")
        raise
