class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_value= prices[0] # just an initialization val
        for price in prices:
            profit = price - lowest_value
            if profit > max_profit:
                max_profit = profit
            if price < lowest_value:
                lowest_value = price
        return max_profit

        