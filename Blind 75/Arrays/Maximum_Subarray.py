class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = nums[0] 
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            global_sum = max(curr_sum, global_sum)
        return global_sum