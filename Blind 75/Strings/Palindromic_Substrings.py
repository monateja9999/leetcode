class Solution:
    def CountPalindromes(self, s, l, r):
            res = 0
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            return res
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.CountPalindromes(s, i, i)
            ans += self.CountPalindromes(s, i, i+1)
        return ans