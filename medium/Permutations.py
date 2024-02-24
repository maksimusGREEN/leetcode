# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used)
                    used[i] = False
                    path.pop()
        
        result = []
        used = [False]*len(nums)
        backtrack([], used)
    
        return result
