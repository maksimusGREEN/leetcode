# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l<=r:
            mid = l+(r-l)//2

            if target==nums[mid]:
                return mid
            
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1
        