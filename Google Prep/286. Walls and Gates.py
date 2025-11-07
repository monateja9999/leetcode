from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        INF = 2147483647
        if not rooms:
            return INF
        rows, cols = len(rooms),len(rooms[0])
        directions = ((0, 1),(0, -1),(1, 0),(-1, 0))
        q = collections.deque([])
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    q.append((row, col))
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy
                    if next_x in range(rows) and next_y in range(cols) and rooms[next_x][next_y] == INF:
                        rooms[next_x][next_y] = rooms[x][y] + 1
                        q.append((next_x, next_y))
        return rooms 