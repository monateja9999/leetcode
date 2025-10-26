class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                check = board[row][col]
                if check ==".": continue
                check_grid = (row // 3 * 3) + col // 3
                if check in rows[row] or check in cols[col] or check in grids[check_grid]:
                    return False
                rows[row].add(check)
                cols[col].add(check)
                grids[check_grid].add(check)
        return True