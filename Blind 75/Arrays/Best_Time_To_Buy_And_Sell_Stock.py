class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-buy)
            if prices[i] < buy:
                buy = prices[i]
        return profit