from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_to_val_freq = {}
        self.freq_to_key = defaultdict(OrderedDict)
        self.min_frequency = 1
    
    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        
        value, freq = self.key_to_val_freq[key]
        del self.key_to_val_freq[key]
        del self.freq_to_key[freq][key]

        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]
            if self.min_frequency == freq:
                self.min_frequency += 1
        
        self.key_to_val_freq[key] = (value, freq + 1)
        self.freq_to_key[freq + 1][key] = None
        return value

    def put(self, key: int, val: int) -> None:
        if self.capacity == 0:
            return 
        
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (val, self.key_to_val_freq[key][1])
            self.get(key)
            return

        if self.size == self.capacity:
            evict_key, _ = self.freq_to_key[self.min_frequency].popitem(last=False)
            del self.key_to_val_freq[evict_key]
            if not self.freq_to_key[self.min_frequency]:
                del self.freq_to_key[self.min_frequency]
            self.size -= 1
        
        self.key_to_val_freq[key] = (val, 1)
        self.freq_to_key[1][key] = None
        self.size += 1
        self.min_frequency = 1

# Driver code
if __name__ == "__main__":
    lfu = LFUCache(3)  # Create an LFU Cache with capacity 3
    
    lfu.put(1, 1)      # Cache is {1=1}
    lfu.put(2, 2)      # Cache is {1=1, 2=2}
    lfu.put(3, 3)      # Cache is {1=1, 2=2, 3=3}
    
    print(lfu.get(2))  # Returns 2, Cache is {1=1, 3=3, 2=2}
    
    lfu.put(4, 4)      # Evicts key 1, Cache is {3=3, 2=2, 4=4}
    print(lfu.get(1))  # Returns -1 (not found)
    
    print(lfu.get(3))  # Returns 3, Cache is {2=2, 4=4, 3=3}
    print(lfu.get(4))  # Returns 4, Cache is {2=2, 3=3, 4=4}
    
    lfu.put(5, 5)      # Evicts key 2, Cache is {3=3, 4=4, 5=5}
    print(lfu.get(2))  # Returns -1 (not found)
