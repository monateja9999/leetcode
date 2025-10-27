class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if m < n:
            return False
        freq = [0] * 26
        for chr in s1:
            freq[ord(chr) - ord('a')] -= 1
        for i in range(n):
            freq[ord(s2[i]) - ord('a')] += 1
        if freq == [0] * 26: return True
        for idx in range(n, m):
            freq[ord(s2[idx - n]) - ord('a')] -= 1
            freq[ord(s2[idx]) - ord('a')] += 1
            if freq == [0] * 26: return True
        return False