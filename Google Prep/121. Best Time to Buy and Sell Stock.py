class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_min = prices[0]
        max_profit = 0
        for price in prices:
            pre_min = min(pre_min, price)
            max_profit = max(max_profit, price - pre_min)
        return max_profit