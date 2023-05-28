import unittest
from cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache2 = LRUCache(1)
        self.cache3 = LRUCache(2)
        self.cache4 = LRUCache(2)

    def test_invalid_capacity(self):
        self.assertRaises(ValueError, LRUCache, 0)
        self.assertRaises(ValueError, LRUCache, -50)

    def test_case_from_task(self):
        self.cache3.set("k1", "val1")
        self.cache3.set("k2", "val2")
        self.assertEqual(self.cache3.get("k3"), None)
        self.assertEqual(self.cache3.get("k2"), "val2")
        self.assertEqual(self.cache3.get("k1"), "val1")
        self.cache3.set("k3", "val3")
        self.assertEqual(self.cache3.get("k3"), "val3")
        self.assertEqual(self.cache3.get("k2"), None)
        self.assertEqual(self.cache3.get("k1"), "val1")

    def test_cache_capacity_1(self):
        self.cache2.set("key1", "value1")
        self.assertEqual(self.cache2.get("key1"), "value1")
        self.cache2.set("key2", "value2")
        self.assertEqual(self.cache2.get("key1"), None)
        self.assertEqual(self.cache2.get("key2"), "value2")

    def test_update_existing_key(self):
        self.cache4.set("k1", "val1")
        self.cache4.set("k2", "val2")

        self.cache4.set("k2", "val2_updated")
        self.assertEqual(self.cache4.get("k2"), "val2_updated")

        self.cache4.set("k3", "val3")
        self.assertEqual(self.cache4.get("k1"), None)
        self.assertEqual(self.cache4.get("k2"), "val2_updated")
        self.assertEqual(self.cache4.get("k3"), "val3")


if __name__ == '__main__':
    unittest.main()
