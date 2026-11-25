class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # buy low, sell high
        max_profit = 0
        for i in range(len(prices)):
            j = i+1
            while j < len(prices) and prices[j] - prices[i] >= 0:
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
                j += 1
        return max_profit