class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        nc = set()
        def dfs(r, c, nc):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O" or (r,c) in nc:
                return
            nc.add((r,c))
            for dx, dy in directions:
                dfs(r+dx, c+dy, nc)
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0, nc)
            if board[row][cols-1] == "O":
                dfs(row, cols-1, nc)
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0, col, nc)
            if board[rows-1][col] == "O":
                dfs(rows - 1, col, nc)
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in nc and board[row][col] == "O":
                    board[row][col] = "X"
        return board