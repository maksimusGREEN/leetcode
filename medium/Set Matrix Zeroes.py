# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place with const extra space.

from typing import List

class Solution:
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        f_row_is_zero = False
        f_col_is_zero = False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0]==0:
                f_col_is_zero=True
                break

        for j in range(n):
            if matrix[0][j]==0:
                f_row_is_zero=True
                break        
 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

        for i in range(1, m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0

        for j in range(1, n):
            if matrix[0][j]==0:
                for i in range(1, m):
                    matrix[i][j]=0

        if f_row_is_zero:
            for j in range(n):
                matrix[0][j]=0

        if f_col_is_zero:
            for i in range(m):
                matrix[i][0]=0
        

        return matrix





