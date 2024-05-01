# Given an integer array nums, return the length of the longest strictly increasing subsequence.

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        n = len(nums)

        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

