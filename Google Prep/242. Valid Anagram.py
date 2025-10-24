class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = [0]*26
        for chr in s:
            check[ord(chr) - ord('a')] += 1
        for chr in t:
            check[ord(chr) - ord('a')] -= 1
        for count in check:
            if count != 0:
                return False
        return True