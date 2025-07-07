class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_seq = 0
        for num in numSet:
            if num - 1 not in numSet:
                seq_len = 1
                while num + seq_len in numSet:
                    seq_len += 1
                max_seq = max(max_seq, seq_len)
        return max_seq