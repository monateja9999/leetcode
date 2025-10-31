from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        time = 0
        heap = [-count for task, count in freq.items()]
        heapq.heapify(heap)
        q = deque()
        while heap or q:
            time += 1
            if heap:
                curr = heapq.heappop(heap) + 1
                if curr < 0:
                    q.append((curr, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time

# Faster Solution: Formula

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         freq = [0] * 26
#         for task in tasks:
#             freq[ord(task) - ord("A")] += 1
#         max_freq = max(freq)
#         max_count = freq.count(max_freq)
#         return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)