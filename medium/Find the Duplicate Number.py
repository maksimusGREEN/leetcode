# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = nums[0]
        tortle = nums[0]

        while True:
            tortle = nums[tortle] 
            hare = nums[nums[hare]]
            if tortle==hare:
                break
        
        ptr_1 = nums[0]
        ptr_2 = tortle

        while ptr_1!=ptr_2:
            ptr_1 = nums[ptr_1]
            ptr_2 = nums[ptr_2]
        
        return ptr_1
