import unittest
from time import sleep
from app.core.cache import Cache

class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache = Cache(100, 36000)
        self.short_cache = Cache(100, 1) # Simulate cache eviction

    def test_cache_set_and_get(self):
        key = "test_key"
        value = "test_value"
        self.cache.set(key, value)
        self.assertEqual(self.cache.get(key), value, "Cache should return the correct value after set")

    def test_cache_get_miss(self):
        key = "non_existent_key"
        self.assertIsNone(self.cache.get(key), "Cache should return None for a miss")

    def test_cache_ttl_expiry(self):
        key = "expiring_key"
        value = "expiring_value"
        self.short_cache.set(key, value)
        # Wait for more than 1 hour (ttl) - for the sake of the test, we will simulate the wait
        sleep(1.1)
        self.assertIsNone(self.cache.get(key), "Cache should return None after the TTL has expired")

    def test_cache_eviction(self):
        # Fill the cache to its max size
        for i in range(100):
            self.cache.set(f"key_{i}", f"value_{i}")

        # Add one more item to trigger eviction
        self.cache.set("extra_key", "extra_value")

        # Check that the extra key is in the cache
        self.assertEqual(self.cache.get("extra_key"), "extra_value", "Cache should contain the newly added item")

        # Since the cache has a max size of 100, ensure at least one of the original items has been evicted
        eviction_occurred = any(self.cache.get(f"key_{i}") is None for i in range(100))
        self.assertTrue(eviction_occurred, "Cache should evict at least one old item when max size is exceeded")

if __name__ == '__main__':
    unittest.main()
