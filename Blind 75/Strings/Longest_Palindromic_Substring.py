class Solution:
    def checkMaxPalindrome(self, s, l , r, res, curr_max):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if((r - l + 1) > curr_max):
                res = s[l : r + 1]
                curr_max = r - l + 1
            l-=1
            r+=1
        return res, curr_max
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        maxLength = 0
        for i in range(len(s)):
            ans, maxLength = self.checkMaxPalindrome(s, i, i, ans, maxLength)
            ans, maxLength = self.checkMaxPalindrome(s, i, i+1, ans, maxLength)
        return ans