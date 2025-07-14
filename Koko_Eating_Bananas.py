class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        left, right = 1, res
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid - 1
        return res 