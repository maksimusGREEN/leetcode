# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Could you do it in-place with O(1) extra space

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k >= len(nums):
            k = k % len(nums)

        def reverse_inplace_arr(lp, rp):
            while lp<rp:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp +=1
                rp -= 1


        reverse_inplace_arr(0, len(nums)-1)
        reverse_inplace_arr(0, k-1)
        reverse_inplace_arr(k, len(nums)-1)
