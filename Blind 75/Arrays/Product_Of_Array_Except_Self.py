class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod, suff_prod = 1, 1
        n = len(nums)
        res = [1] * n
        for i in range(n):
            res[i] *= pre_prod
            res[n-i-1] *= suff_prod
            pre_prod *= nums[i]
            suff_prod *= nums[n-1-i]
        return res