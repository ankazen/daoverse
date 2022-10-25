import asyncio_redis
from strdata import config

class Redis:
    _pool = None
    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                    host=config.REDIS_HOST, port=config.REDIS_PORT, poolsize=config.REDIS_POOLSIZE
                )
        return self._pool
