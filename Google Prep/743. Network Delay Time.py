class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        minHeap = [(0, k)]
        visited = set()
        time = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, weight)
            for w, v in graph[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (weight + w, v))
        return time if len(visited) == n else -1