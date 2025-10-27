class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = right_max = water = 0
        left, right = 0, n - 1
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            check = min(left_max, right_max)
            if height[left] < height[right]:
                water += check - height[left]
                left += 1
            else:
                water += check - height[right]
                right -= 1
        return water