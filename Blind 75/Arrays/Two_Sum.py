class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            check = target - nums[i] 
            if check in d:
                return [d[check],i]
            d[nums[i]] = i