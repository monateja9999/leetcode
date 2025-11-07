from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {node : [] for node in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited or not dfs(neighbour, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
        