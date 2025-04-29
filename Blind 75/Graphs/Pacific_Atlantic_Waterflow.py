class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, visited, prevHeight):
            if r <0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
                
        for row in range(rows):
            dfs(row,0,pac,heights[row][0])
            dfs(row,cols-1,atl,heights[row][cols-1])
        for col in range(cols):
            dfs(0,col,pac,heights[0][col])
            dfs(rows-1,col,atl,heights[rows-1][col])
        
        return list(pac & atl)