import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        n, m = len(self.maxheap), len(self.minheap)
        if n - m == 0:
            if n == 0 or num <= self.minheap[0]:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
        else:
            if num >= -self.maxheap[0]:
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                heapq.heappush(self.maxheap, -num)

    def findMedian(self) -> float:
        n, m = len(self.maxheap), len(self.minheap)
        if (n + m) % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Solution 2 (Same Complexity)

# from sortedcontainers import SortedList
# class MedianFinder:

#     def __init__(self):
#         self.arr = SortedList([])

#     def addNum(self, num: int) -> None:
#         self.arr.add(num)
        
#     def findMedian(self) -> float:
#         mid = len(self.arr)//2
#         if len(self.arr) % 2 == 0:
#            return (self.arr[mid] + self.arr[mid-1]) / 2
#         else:
#             return self.arr[mid]
        
