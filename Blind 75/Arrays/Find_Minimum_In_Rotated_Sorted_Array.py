class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        res = sys.maxsize
        while left <= right:
            mid = ( left + right ) // 2
            if nums[left] <= nums[mid]:
                res = min(res, nums[left])
                left = mid + 1
            else:
                res = min(res, nums[mid])
                right = mid - 1
        return res