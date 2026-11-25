class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_val = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max_val: max_val = prices[j]-prices[i]
        # return max_val

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                if prices[r] - prices[l] > max_profit:
                    max_profit = prices[r] - prices[l]
                r += 1
        return max_profit
