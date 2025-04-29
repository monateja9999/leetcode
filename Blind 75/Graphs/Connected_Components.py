class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}
        visited = set()
        components = 0

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        for node in graph:
            if node not in visited:
                dfs(node)
                components+=1
        return components