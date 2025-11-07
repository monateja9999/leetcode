from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        graph = {node : [] for node in range(n)}
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        def bfs(node):
            q = collections.deque([node])
            while q:
                curr = q.popleft()
                visited.add(curr)
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        q.append(neighbour)

        components = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                components += 1
        return components