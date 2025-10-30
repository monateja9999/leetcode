class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0 , m * n - 1
        while left <= right:
            mid = (left + right ) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# Solution 2
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         def search_idx(nums, target):
#             left, right = 0, len(nums)
#             while left < right:
#                 mid = (left + right) // 2
#                 if nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid
#             return left
#         m, n = len(matrix), len(matrix[0])
#         first_col = [matrix[row][0] for row in range(m)]
#         check_row = search_idx(first_col, target)

#         if 0 <= check_row < m and matrix[check_row][0] == target:
#             return True
#         else:
#             check_row -= 1
#             req = search_idx(matrix[check_row], target)
#             if 0 <= req < n and matrix[check_row][req] == target:
#                 return True
#             else:
#                 return False