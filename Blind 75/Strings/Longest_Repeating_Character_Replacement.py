class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=collections.defaultdict(int)
        max_Length = 0
        max_Freq = 0
        left = 0
        right = 0

        while right < len(s):
            d[s[right]]+=1
            max_Freq = max(max_Freq,d[s[right]])
            window_Size = right - left + 1
            req_Swaps = window_Size - max_Freq
            if req_Swaps <= k:
                max_Length = max(max_Length, window_Size)
            else:
                d[s[left]]-= 1
                left+=1
                max_Freq -= 1
            right+=1
        return max_Length