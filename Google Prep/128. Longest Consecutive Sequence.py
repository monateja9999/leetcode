class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        max_len = 0
        for num in visited:
            if num - 1 not in visited:
                check = num
                arr_len = 0
                while check in visited:
                    arr_len += 1
                    check += 1
                max_len = max(max_len, arr_len)
        return max_len