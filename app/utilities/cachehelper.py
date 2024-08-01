import hashlib
import logging
import requests  # Make sure to import the requests library
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CACHE_SERVER_URL = 'http://localhost:5001/cache'

class CacheHelper:
    def get(self, key):
        response = requests.get(f"{CACHE_SERVER_URL}/{key}")
        if response.status_code == 200:
            logger.info("Cache Hit!")
            return response.json()['value']
        return None

    def set(self, key, value):
        response = requests.post(f"{CACHE_SERVER_URL}/{key}", json={'value': value})
        logger.info("Cache SET!")
        return response.status_code == 201

    def delete(self, key):
        response = requests.delete(f"{CACHE_SERVER_URL}/{key}")
        return response.status_code == 200