# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
                return res
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res
        

        def twoSum(nums, target):
            res = []
            seen = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in seen:
                        res.append([target - nums[i], nums[i]])
                seen.add(nums[i])
            return res


        nums.sort()
        
        return kSum(nums, target, 4)