class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        output = []
        while left < right and top < bottom:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            
            right -= 1
            
            if not (top < bottom and left < right):
                break
            
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i])
            
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][left])
            
            left += 1
        return output