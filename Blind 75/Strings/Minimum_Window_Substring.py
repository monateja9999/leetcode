class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = count = start = 0
        min_len = sys.maxsize
        d = collections.Counter(t)
        target = len(t)
        while right < len(s):
            d[s[right]] -= 1
            if d[s[right]] >= 0:
                count += 1
                while count == target:
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        start = left
                    d[s[left]] +=  1
                    if d[s[left]] > 0:
                        count -= 1
                    left += 1                   
            right += 1
        return s[start : start + min_len] if min_len < sys.maxsize else ""