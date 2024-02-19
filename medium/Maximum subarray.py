# Given an integer array nums, find the 
# subarray with the largest sum, and return its sum.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]
        ans = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            ans = max(ans, dp[i])
        return ans
        