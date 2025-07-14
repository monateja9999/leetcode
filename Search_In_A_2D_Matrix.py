class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1 
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        if bottom < 0:
            return False
        left, right = 0, len(matrix[bottom]) - 1 
        while left <= right:
            mid = (left + right) // 2
            if matrix[bottom][mid] == target:
                return True
            elif matrix[bottom][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False