class LRU_Cache:
    """
    LRU_Cache holds a cache of given capacity in order to reduce time-complexity.
    Useful for maintaining values that may be used repeatedly by multiple functions.    
    """
    def __init__(self, capacity):
        if capacity <= 0:
          raise ValueError('Capacity of cache must be greater than 0')
        self.key_cache = {}
        self.used_cache = []
        self.capacity = capacity


    def get(self, key):
        if key in self.key_cache:
            #key in cache, so update used_cache and return value
            self.used_cache.remove(key)
            self.used_cache.append(key)
            return self.key_cache[key]
        else:
          return -1


    def set(self, key, value):
        if len(self.key_cache) == self.capacity:
          release = self.used_cache[0]
          self.key_cache.pop(release)
          self.used_cache.remove(release)

          self.key_cache[key] = value
          self.used_cache.append(key)
        else:
          if key in self.key_cache:
            self.key_cache[key] = value

            self.used_cache.remove(key)
            self.used_cache.append(key)

          self.key_cache[key] = value
          self.used_cache.append(key)


if __name__ == '__main__':
  our_cache = LRU_Cache(5)

  our_cache.set(1, 1);
  our_cache.set(2, 2);
  our_cache.set(3, 3);
  our_cache.set(4, 4);


  our_cache.get(1)       # returns 1
  our_cache.get(2)       # returns 2
  our_cache.get(9)      # returns -1 because 9 is not present in the cache

  our_cache.set(5, 5) 
  our_cache.set(6, 6)

  our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
