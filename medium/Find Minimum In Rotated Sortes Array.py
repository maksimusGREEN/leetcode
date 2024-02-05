# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

from typing import List

class Solution:
    
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        if len(nums)==1:
            return nums[0]

        if nums[l]<nums[r]:
            return nums[l]

        while l<=r:

            mid = (l+r) // 2

            if nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid-1
            
