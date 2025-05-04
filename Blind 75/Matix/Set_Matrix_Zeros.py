class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = 1

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        rowZero = 0
                    else: 
                        matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(1, rows):
            for col in range(1,cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0
        if rowZero == 0:
            for col in range(cols):
                matrix[0][col] = 0
        return matrix