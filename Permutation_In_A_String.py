class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        def to_freq_array(s: str) -> list:
            freq = [0] * 26
            for chr in s:
                freq[ord(chr) - ord('a')] += 1
            return freq
        
        s1_check = to_freq_array(s1)
        s2_check = to_freq_array(s2[:len(s1)])

        if s1_check == s2_check:
            return True
        
        for i in range(len(s1), len(s2)):
            
            s2_check[ord(s2[i-len(s1)]) - ord('a')] -= 1
            s2_check[ord(s2[i]) - ord('a')] += 1

            if s1_check == s2_check:
                return True
        return False        