# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        queue = deque()

        row_max, col_max = len(mat)-1, len(mat[0])-1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    mat[i][j]=-1

        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<=row_max and 0<=new_y<=col_max and mat[new_x][new_y]==-1:
                    mat[new_x][new_y] = mat[x][y]+1
                    queue.append((new_x, new_y))
        
        return mat
        