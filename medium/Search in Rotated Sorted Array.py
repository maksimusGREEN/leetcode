# There is an integer array nums sorted in ascending order (with distinct values).

# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search_border(nums):

            l, r = 0, len(nums)-1

            while l<r:
                mid = l+(r-l)//2
                if nums[mid]>nums[r]:
                    l = mid+1
                else:
                    r = mid
            return l
        
        def bin_search(left, right):

            while left<=right:
                mid = left+(right-left)//2

                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        
        p = search_border(nums)

        if p==0:
            return bin_search(0, len(nums)-1)
        else:
            if target==nums[0]:
                return 0
            elif target>nums[0]:
                return bin_search(0, p-1)
            else:
                return bin_search(p, len(nums)-1)


