"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}

        def dfs(original):
            if original in d:
                return d[original]
            copy = Node(original.val)
            d[original] = copy
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None