class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res
        left, right = 0, len(self.store[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][1] <= timestamp:
                res = self.store[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# Solution 2

# import bisect
# from collections import defaultdict

# class TimeMap:

#     def __init__(self):
#         self.store = defaultdict(list)
        
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.store[key].append((value, timestamp))
        
#     def get(self, key: str, timestamp: int) -> str:
#         if key not in self.store:
#             return ""
#         idx = bisect.bisect_right(self.store[key], timestamp, key=lambda x: x[1])
#         if idx == 0:
#             return ""
#         return self.store[key][idx-1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)