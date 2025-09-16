class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        res = 0
        while low <= high:
            mid = (low + high) // 2
            mid_square = mid * mid
            if mid_square == x:
                return mid
            elif mid_square < x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
