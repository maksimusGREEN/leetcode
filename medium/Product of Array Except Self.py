# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        for i in range(1, len(nums)):
            left_prod[i] = nums[i-1]*left_prod[i-1]
        for i in range(len(nums)-2,-1,-1):
            right_prod[i] = right_prod[i+1]*nums[i+1]
        return [i*j for i, j in zip(left_prod, right_prod)]
    

print(Solution().productExceptSelf([1,2,3,4]))