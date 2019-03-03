from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices = []:
            return 0

        profit = 0
        high = prices[0]
        low = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                profit += high - low
                low = prices[i]
                high = prices[i]
            elif prices[i] >= prices[i - 1]:
                high = prices[i]

        profit += high - low
        return profit
