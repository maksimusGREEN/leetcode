# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money. 
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1. 
# You may assume that you have an infinite number of each kind of coin.


from typing import List

class Solution:
    def coinChange(self, coins: List, amount: int) -> int:
        # Create an array to store the fewest number of coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins are needed to make up 0 amount

        # Iterate through each coin and update the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
    

print(Solution().coinChange([186,419,83,408], 6249))
