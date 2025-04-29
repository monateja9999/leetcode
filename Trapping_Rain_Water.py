class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0 , n-1
        left_max, right_max = -1, -1
        water = 0

        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if height[left] < height[right]:
                water+= left_max - height[left]
                left+=1
            else:
                water+=  right_max - height[right]
                right-=1

        return water