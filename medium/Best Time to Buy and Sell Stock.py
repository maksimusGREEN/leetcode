# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = float('-inf')
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p-min_price)
        return max_profit
    

print(Solution().maxProfit([1,2,3,4,5,6]))