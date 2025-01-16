class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for i in prices[1:]:
            max_profit = max(i - min_price, max_profit)
            if i < min_price:
                min_price = i
        
        return max_profit
