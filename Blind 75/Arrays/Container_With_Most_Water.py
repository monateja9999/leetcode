class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        low = 0
        high = n - 1
        ans = 0

        while low < high:
            h = min(height[low], height[high])
            w = high - low
            a = h*w
            ans = max(ans, a)

            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
        return ans