
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
     
        adj = {point: [] for point in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        minHeap = [(0, 0)]
        visited = set()
        cost = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            cost += weight
            for w, v in adj[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (w, v))
        return cost

# O (N^2)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges, ans, node = 0, 0, 0
        n = len(points)
        visited = [False] * n
        distances = [float("inf")] * n

        while edges < n - 1:
            nextNode = -1
            visited[node] = True
            for i in range(n):
                if visited[i]:
                    continue
                curr_dist = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                distances[i] = min(distances[i], curr_dist)
                if nextNode == - 1 or distances[i] < distances[nextNode]:
                    nextNode = i
            ans += distances[nextNode]
            node = nextNode    
            edges += 1 
        return ans