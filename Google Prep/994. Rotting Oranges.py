class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotting_oranges = collections.deque()
        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1), (0,-1), (1, 0), (-1, 0))
        fresh_count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1
                if grid[row][col] == 2:
                    rotting_oranges.append((row, col))
        if fresh_count == 0:
            return 0
        time = 0
        while rotting_oranges:
            rotted = False
            for i in range(len(rotting_oranges)):
                x, y = rotting_oranges.popleft()                
                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy

                    if next_x in range(rows) and next_y in range(cols) and grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        fresh_count -= 1
                        rotting_oranges.append((next_x, next_y))
                        rotted = True
            if rotted:
                time += 1
        if fresh_count == 0:
            return time
        else:
            return -1