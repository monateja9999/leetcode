class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        targetLength = len(t)
        count = 0
        minLength = sys.maxsize
        start = 0
        d = collections.Counter(t)
        while r < len(s):
            d[s[r]] -= 1
            if d[s[r]] >= 0:
                count += 1
                while count == targetLength:
                    if (r - l + 1) < minLength:
                        minLength = min(minLength, r - l + 1)
                        start = l      
                    d[s[l]] += 1
                    if(d[s[l]] > 0):
                        count -= 1
                    l += 1        
            r += 1
        if minLength < sys.maxsize:
            return s[start:start+minLength]
        else:
            return ""