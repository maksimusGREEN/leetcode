# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        ans = []
        queue = deque([root])
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(level)
        return ans


            