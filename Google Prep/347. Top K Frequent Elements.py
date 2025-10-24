from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        maxi = max(c.values())
        buckets = [[] for _ in range(maxi+1)]
        for key, freq in c.items():
            buckets[freq].append(key)
        count = 0
        ans = []
        for idx in range(maxi, -1, -1):
            for ele in buckets[idx]:
                if len(ans) == k:
                    break
                ans.append(ele)
            if len(ans) == k:
                    break    
        return ans