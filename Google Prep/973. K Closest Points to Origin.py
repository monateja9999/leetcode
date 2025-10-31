import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            heapq.heappush(heap, (-(x*x + y*y),x,y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = [[y,z] for x,y,z in heap]
        return res