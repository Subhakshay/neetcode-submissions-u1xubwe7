class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        

        for left in range(len(prices)):
            right = len(prices) - 1
            while left < right :
                max_profit = prices[right] - prices[left]
                profit = max(max_profit, profit)
                right -= 1
        return profit
