# You are given an m x n integer array grid. 
# There is a robot initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. 
# A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.


from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]

        # base cases
        for col in range(n):
            if obstacleGrid[0][col]==1:
                break
            dp[0][col] = 1
        
        for row in range(m):
            if obstacleGrid[row][0]==1:
                break
            dp[row][0] = 1  

        for row in range(1,m):
            for col in range(1,n):
                if obstacleGrid[row][col]==0:
                    dp[row][col] = dp[row-1][col]+dp[row][col-1]
        
        return dp[-1][-1]