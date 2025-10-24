class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for idx, num in enumerate(nums):
            check = target - num
            if check in visited:
                return [visited[check], idx]
            visited[num] = idx