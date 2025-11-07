class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        if not grid:
            return max_area
        rows, cols = len(grid), len(grid[0])
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        def bfs(r,c):
            q = collections.deque([(r,c)])
            grid[r][c] = 0
            area = 1
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy
                    if next_x in range(rows) and next_y in range(cols) and grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 0
                        area += 1
                        q.append((next_x, next_y))
            return area
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    curr_area = bfs(row,col)
                    max_area = max(max_area, curr_area)
        return max_area