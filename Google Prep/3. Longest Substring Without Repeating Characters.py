class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = max_len = 0
        substr = set()
        while right < len(s):
            if s[right] in substr:
                substr.remove(s[left])
                left += 1
            else:
                substr.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
        return max_len