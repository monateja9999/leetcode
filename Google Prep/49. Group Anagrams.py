from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strs:
            freq = [0] * 26
            for chr in string:
                freq[ord(chr) - ord('a')] += 1
            d[tuple(freq)].append(string)
        return list(d.values())