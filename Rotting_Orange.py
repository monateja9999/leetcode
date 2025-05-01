class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        queue = deque()
        fresh = 0
        time = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col,0))
                elif grid[row][col] == 1:
                    fresh += 1
            
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)

            for dr,dc in directions:
                if 0 <= r+dr < rows and 0 <= dc+c < cols and grid[r+dr][c+dc] == 1:
                    queue.append((r+dr, c+dc, t+1))
                    grid[r+dr][c+dc] = 2
                    fresh -=1
        return time if fresh == 0 else -1