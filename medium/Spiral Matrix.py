# Given an m x n matrix, return all elements of the matrix in spiral order.


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []

        top, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

        while top<=down and left<=right:

            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1

            for i in range(top, down+1):
                ans.append(matrix[i][right])
            right-=1

            if top<=down:
                for i in range(right, left-1, -1):
                    ans.append(matrix[down][i])
                down-=1

            if left<=right:
                for i in range(down, top-1, -1):
                    ans.append(matrix[i][left])
                left+=1

        return ans
    
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))