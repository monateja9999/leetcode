class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        tree = {i:[] for i in range(n)}
        visited = set()
        for x,y in edges:
            tree[x].append(y)
            tree[y].append(x)

        stack = collections.deque()
        stack.append((0,-1))

        while stack:
            node, parent = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in tree[node]:
                    if neighbor != parent:
                        stack.append((neighbor,node))
        return len(visited) == n