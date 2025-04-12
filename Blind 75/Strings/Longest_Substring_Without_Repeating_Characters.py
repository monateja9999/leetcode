class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_Length = 0
        left = -1
        right = 0
        while(right < len(s)):
            if s[right] in d:
                if d[s[right]] > left:
                    left = d[s[right]]
                d[s[right]] = right
            else:
                d[s[right]] = right
            max_Length = max(max_Length,right-left)
            right += 1
        return max_Length