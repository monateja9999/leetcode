class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(map(str,s.strip().split()))
        l.reverse()
        return " ".join(l)