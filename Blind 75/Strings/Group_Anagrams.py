class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for string in strs:
            check = [0] * 26
            for chr in string:
                check[ord(chr) - 97] += 1
            temp = tuple(check)
            d[temp].append(string)
        return [val for key, val in d.items()]        