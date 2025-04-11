class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_prod = 1
        suff_prod = 1
        ans = -inf
        n = len(nums)
        for i in range(n):
            if pre_prod == 0:
                pre_prod = 1
            if suff_prod == 0:
                suff_prod = 1
            pre_prod *= nums[i]
            suff_prod *= nums[n-i-1]
            ans = max(ans, max(pre_prod, suff_prod))
        return ans