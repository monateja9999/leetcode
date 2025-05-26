class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsums = collections.defaultdict(int)
        prefixsums[0] = 1
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in prefixsums:
                count += prefixsums[cur_sum - k]
            prefixsums[cur_sum]+=1
        return count