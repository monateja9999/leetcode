class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        max_freq, max_len = 0, 0 
        left, right = 0, 0
        while right < len(s):
            if s[right] not in d:
                d[s[right]] = 1
            else:
                d[s[right]] += 1
            max_freq = max(max_freq, d[s[right]])
            if (right - left + 1) - max_freq > k:
                d[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len