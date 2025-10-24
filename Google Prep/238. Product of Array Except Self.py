class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, pre_prod, post_prod = [1]*n, 1, 1
        for i in range(n):
            ans[i] *= pre_prod
            pre_prod *= nums[i]
            ans[n-1-i] *= post_prod
            post_prod *= nums[n-1-i]
        return ans