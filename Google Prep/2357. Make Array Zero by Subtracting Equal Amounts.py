class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = set(nums)
        res.discard(0)
        return len(res)