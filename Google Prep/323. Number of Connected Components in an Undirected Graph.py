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
            visited.add(node)
            while q:
                curr = q.popleft()
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)

        components = 0
        for node in range(n):
            if node not in visited:
                bfs(node)
                components += 1
        return components

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
        par = [node for node in range(n)]
        rank = [1] * n
        
        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        res = n

        for n1,n2 in edges:
            res -= union(n1,n2)
        return res


