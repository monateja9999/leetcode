class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def dfs(x,y):
            if x not in range(rows) or y not in range(cols) or grid[x][y] == "0":
                return  
            grid[x][y] = "0"
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        def dfs(x,y):
            q = collections.deque([(x,y)])
            grid[x][y] = "0"
            while q:
                curr_x, curr_y = q.popleft()
                for dx,dy in directions:
                    next_x = curr_x + dx
                    next_y = curr_y + dy
                    if next_x in range(rows) and next_y in range(cols) and grid[next_x][next_y] == "1":
                        grid[next_x][next_y] = "0"
                        q.append((next_x,next_y))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands