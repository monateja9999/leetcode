class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subSum = sum(arr[:k])
        count = 0
        if subSum / k >= threshold:
            count += 1
        for i in range(k,len(arr)):
            subSum = -(arr[i-k]) + subSum + arr[i]
            if subSum / k >= threshold:
                count += 1
        return count