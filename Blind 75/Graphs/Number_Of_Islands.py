class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row,col):
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                directions = [[0,-1],[0,1],[1,0],[-1,0]]

                for dr,dc in directions:
                    r=row+dr
                    c=col+dc

                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == "1":
                        q.append((r,c))
                        visited.add((r,c))
            
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    bfs(row,col)
                    islands +=1
        return islands