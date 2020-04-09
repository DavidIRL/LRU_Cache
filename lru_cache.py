class LRU_Cache():
    """ 
    LRU_Cache holds a cache of given size (capacity) in order to reduce
    \n time_complexity within separate functions that would need to call
    \n repeatedly on different values
    """
    
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError('Capacity must be greater than 0')
        # a dict for holding key/value pairs
        self.key_cache = {}
        # a list for tracking LRU - index 0 being least used element
        self.use_cache = []
        self.capacity = capacity
     
    
    def get(self, key):
        if key in self.key_cache:
            # key in cache so get keys value and update use
            self.use_cache.remove(key)
            self.use_cache.append(key)
            return self.key_cache[key]
        else:
            return -1 # key not in cache
        
              
    def set(self, key, value):
        if len(self.key_cache) == self.capacity:
            lru = self.use_cache[0]
            # remove least used from both dicts
            self.key_cache.pop(lru)
            self.use_cache.remove(lru)
            # add new key, value and set uses to 1
            self.key_cache[key] = value
            self.use_cache.append(key)
        else:    
            if key in self.key_cache:
                self.key_cache[key] = value
                # pull key from use list and append to end (meaning most recently used)
                self.use_cache.remove(key)
                self.use_cache.append(key)
            #key not in cache so add and set as most recent used
            self.key_cache[key] = value
            self.use_cache.append(key)

if __name__ == '__main__':
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print(our_cache.get(1))    # returns 1
    print(our_cache.get(2))    # returns 2
    print(our_cache.get(9))    # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(our_cache.get(3))    # returns -1 because the cache reached it's capacity
                               # and had to remove the LRU value to make room (3 in this case)

    new_cache = LRU_Cache(0)   # should return ValueError since entered capacity is < 1