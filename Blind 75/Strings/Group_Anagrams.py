class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        for i in range(len(strs)):
            check = [0]*26
            n = len(strs[i])
            if n == 0:
                d["0"].append("")
            else:
                for j in range(n):
                    check[ord(strs[i][j])-97]+=1
                d[','.join(map(str, check))].append(strs[i])
        return list(d.values())