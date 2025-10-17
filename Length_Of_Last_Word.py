class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = list(map(str,s.strip().split(" ")))
        return len(l[-1])
