class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        directions = [[0,1],[-1,0],[1,0],[0,-1]]
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or  c < 0 or r > rows-1 or c > cols-1 or (r,c) in path or board[r][c] != word[i]:
                return False
            path.add((r,c))
            for dr,dc in directions:
                if dfs(r+dr,c+dc,i+1):
                    return True  
            path.remove((r, c)) 
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False