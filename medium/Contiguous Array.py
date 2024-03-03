#Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count_map = {0: -1}  # Initialize with count 0 at index -1
        max_length = 0
        count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i

        return max_length
    
print(Solution().findMaxLength([0,0,1,0,0,0,1,1]))