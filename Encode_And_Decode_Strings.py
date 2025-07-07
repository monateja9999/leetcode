class Solution:
    def encode(self, strs):
        res=""
        for i in range(len(strs)):
            res+= str(len(strs[i]))+ "#" + strs[i]
        return res

    def decode(self, str):
        res, start = [], 0

        while start < len(str):
            end = start
            while str[end] != "#":
                end += 1
            length = int(str[start:end])
            res.append(str[end + 1:end + length + 1])
            start = end + length + 1
        return res