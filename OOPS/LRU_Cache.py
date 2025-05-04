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