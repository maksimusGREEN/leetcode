# Given an integer array nums of unique elements, return all possible 
# subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans += [subset+[num] for subset in ans]

        return ans
    
    def dfs_subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(i, subset):

            ans.append(subset)

            if i < len(nums):
                
                for j in range(i, len(nums)):
                    dfs(j+1, subset+[nums[j]])

        dfs(0, [])

        return ans
