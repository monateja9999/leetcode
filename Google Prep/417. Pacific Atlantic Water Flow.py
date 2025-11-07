class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def bfs(r, c, res):
            q = collections.deque([(r, c)])
            res.add((r, c))
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    next_x, next_y = x + dx, y + dy
                    if next_x in range(rows) and next_y in range(cols) and heights[next_x][next_y] >= heights[x][y] and (next_x, next_y) not in res:
                        q.append((next_x, next_y))
                        res.add((next_x, next_y))
            return res
        
        for r in range(rows):
            bfs(r, 0, pacific)
        for c in range(cols):
            bfs(0, c, pacific)
        for r in range(rows):
            bfs(r, cols - 1, atlantic)
        for c in range(cols):
            bfs(rows - 1, c, atlantic)
        return list(map(list, pacific & atlantic))