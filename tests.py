import unittest

from lru_cache import LRU_Cache

class Tests(unittest.TestCase):
    def test_lru_create(self):
        test_cache = LRU_Cache(5)

        test_cache.set(1, None)
        test_cache.set(2, 3999)
        test_cache.set(3, -33)
        test_cache.set(4, "important")
        
        self.assertEqual(test_cache.get(3), -33)
        self.assertEqual(test_cache.get(1), None)
        self.assertEqual(test_cache.get(4), "important")

        test_cache.set(5, True)
        test_cache.set(6, 9876543210)
        # cache idx 2 should've been removed for 6, so below should return -1
        self.assertEqual(test_cache.get(2), -1)   
        self.assertEqual(test_cache.get(6), 9876543210)


if __name__ == '__main__':
    unittest.main()

