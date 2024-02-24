# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right = 0, len(matrix)-1

        while left<=right:
            mid = left+(right-left)//2

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True

            elif matrix[mid][0] < target < matrix[mid][-1]:
                l, r = 0, len(matrix[0])
                while l<=r:
                    inner_mid = l+(r-l)//2

                    if matrix[mid][inner_mid] == target:
                        return True
                    elif matrix[mid][inner_mid] > target:
                        r = inner_mid-1
                    else:
                        l = inner_mid+1
                return False

            else:
                if target > matrix[mid][-1]:
                    left = mid+1
                elif target < matrix[mid][0]:
                    right = mid-1
        
        return False
    
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))