# Given an integer array nums of unique elements, return all possible 
# subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
    
    def dfs_subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(i, subset):

            ans.append(subset)

            if i < len(nums):
                
                for j in range(i, len(nums)):
                    dfs(j+1, subset+[nums[j]])

        dfs(0, [])

        return ans
