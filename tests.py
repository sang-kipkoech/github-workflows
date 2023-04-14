import unittest
from file import CacheLRU


class CacheLRUTestCase(unittest.TestCase):
    def test_cache_lru(self):
        cache = CacheLRU(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(4, 4)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(1), -1)
        cache.put(5, 5)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), -1)
        self.assertEqual(cache.get(5), 5)
