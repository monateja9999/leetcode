class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = 1
        suff_prod = 1
        n = len(nums)
        output = [1] * n
        for i in range(len(nums)):
            output[i] *= pre_prod
            output[n-i-1] *= suff_prod
            pre_prod *= nums[i]
            suff_prod *= nums[n-1-i]
        return output