from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        for idx, num in enumerate(nums):
            pos = window.bisect_left(num)
            if pos < len(window) and window[pos] - num <= valueDiff:
                return True
            if pos > 0 and  num - window[pos-1] <= valueDiff:
                return True
            window.add(num)
            if len(window) > indexDiff:
                window.remove(nums[idx - indexDiff])
        return False