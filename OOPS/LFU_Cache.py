from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity : int):
        self.capacity = capacity
        self.size = 0
        self.key_to_val_freq = {}
        self.freq_to_key = defaultdict(OrderedDict)
        self.min_frequency = 1
    
    def get(self, key : int) -> int:
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

    def put(self, key : int, val : int) -> None:
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
            self.size -=1
        
        self.key_to_val_freq[key] = (val, 1)
        self.freq_to_key[1][key] = None 
        self.size += 1
        self.min_frequency = 1
    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)