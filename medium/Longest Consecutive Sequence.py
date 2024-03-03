# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)

        max_len = 0

        for num in nums:
            if num-1 not in s:
                cur_num = num
                current_length=1

                while cur_num+1 in s:
                    current_length+=1
                    cur_num+=1
                
                max_len = max(max_len, current_length)
        
        return max_len
