import unittest
from cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_cache(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k2"), "val2")

        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")
        self.assertEqual(cache.get("k2"), None)

        cache.set("k1", "new_val1")
        self.assertEqual(cache.get("k1"), "new_val1")


if __name__ == '__main__':
    unittest.main()
