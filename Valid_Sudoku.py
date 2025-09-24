class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for row in range(len(rows)):
            for col in range(len(cols)):

                if board[row][col] == ".":
                    continue
                
                box_index = (row // 3) * 3 + col // 3

                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[box_index]:
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[box_index].add(board[row][col])
                
        return True
