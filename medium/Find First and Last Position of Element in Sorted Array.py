from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftmost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def findRightmost(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1

        ans = [-1,-1]

        left_index = findLeftmost(nums, target)
        right_index = findRightmost(nums, target)
        
        if left_index<=right_index:
            ans = [left_index, right_index]
        
        return ans

print(Solution().searchRange([2,2], target = 3))