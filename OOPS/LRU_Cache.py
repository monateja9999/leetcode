from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.size = 0
    
    def get(self, key : int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, val: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            self.cache[key] = val
            self.get(key)
            return
        
        if self.size == self.capacity:
            self.cache.popitem(last=False)
            self.size -= 1

        self.cache[key] = val
        self.size += 1


# Driver code
if __name__ == "__main__":
    lru = LRUCache(3)  # Creating an LRU cache with a capacity of 3
    lru.put(1, 1)      # Cache is {1=1}
    lru.put(2, 2)      # Cache is {1=1, 2=2}
    print(lru.get(1))  # Returns 1, Cache is {2=2, 1=1}
    lru.put(3, 3)      # Cache is {2=2, 1=1, 3=3}
    print(lru.get(2))  # Returns 2, Cache is {1=1, 3=3, 2=2}
    lru.put(4, 4)      # Evicts key 1, Cache is {3=3, 2=2, 4=4}
    print(lru.get(1))  # Returns -1 (not found)
    print(lru.get(3))  # Returns 3, Cache is {2=2, 4=4, 3=3}
    print(lru.get(4))  # Returns 4, Cache is {2=2, 3=3, 4=4}
