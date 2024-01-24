#You are given an integer array nums. You are initially positioned at the array's first index,
#and each element in the array represents your maximum jump length at that position.

#Return true if you can reach the last index, or false otherwise.


from typing import List

#greedy algo realization
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_reachable = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=last_reachable:
                last_reachable = i
        return last_reachable==0
        