# Given a binary tree, determine if it is height-balanced.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if not root:
                return 0
            left_depth = helper(root.left)
            right_depth = helper(root.right)
            if left_depth==-1 or right_depth==-1 or abs(left_depth - right_depth)>1:
                return -1
            return max(left_depth, right_depth) + 1

        return helper(root)!=-1
            