class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_min = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(price - pre_min, max_profit)
            pre_min = min(price, pre_min)
        return max_profit