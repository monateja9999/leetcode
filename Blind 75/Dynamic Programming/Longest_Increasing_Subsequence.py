class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        req = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > req[-1]:
                req.append(nums[i])
            else:
                low, high = 0, len(req) - 1

                while low <= high:
                    mid = (low + high) // 2
                    if req[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid - 1
                req[low] = nums[i]
        return len(req) 
         