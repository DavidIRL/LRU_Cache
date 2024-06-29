import unittest

from lru_cache import LRU_Cache

class Tests(unittest.TestCase):
    def test_lru_create1(self):
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


    def test_lru_create2(self):
        test_cache2 = LRU_Cache(3)
        
        test_cache2.set(1,"Soloman Grundy")
        test_cache2.set(2,"Joker")
        
        self.assertEqual(test_cache2.get(3), -1) #3 not in test_cache2
        
        test_cache2.set(3,"Bane")

        self.assertEqual(test_cache2.get(3), "Bane")

        test_cache2.set(4, "Penguin")

        self.assertEqual(test_cache2.get(1), -1) #Soloman should have been replaced by Penguin

        test_cache2.set(4, "You never start with the head, the victim gets all fuzzy. He can't feel the next... see?")
        test_cache2.set(5, 7351857301)

        self.assertEqual(test_cache2.get(4), "You never start with the head, the victim gets all fuzzy. He can't feel the next... see?")


    def test_invalid_create(self):
        with self.assertRaises(ValueError):
            invalid_cache = LRU_Cache(-42)


if __name__ == '__main__':
    unittest.main()

