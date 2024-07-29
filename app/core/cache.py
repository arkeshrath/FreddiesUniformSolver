import logging
from cachetools import TTLCache

# Setup static logger instance
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Cache:
    def __init__(self, maxsize=100, ttl=36000):
        self.cache = TTLCache(maxsize=maxsize, ttl=ttl)
        logger.info("Cache initialized")

    def get(self, key):
        value = self.cache.get(key)
        if value:
            logger.info("Cache hit for key: %s", key)
        else:
            logger.info("Cache miss for key: %s", key)
        return value

    def set(self, key, value):
        self.cache[key] = value
        logger.info("Cache set for key: %s", key)
