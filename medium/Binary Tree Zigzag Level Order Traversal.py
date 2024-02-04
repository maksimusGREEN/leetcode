# Given the root of a binary tree, return the zigzag level order traversal of its nodes values.
# (i.e., from left to right, then right to left for the next level and alternate between).

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        zigzag = False
        ans = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if zigzag:
                level = level[::-1]

            ans.append(level)
            
            zigzag = not zigzag

        return ans