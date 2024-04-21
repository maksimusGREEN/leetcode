# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(root_left, root_right):
            
            if not root_left and not root_right:
                return True

            if not root_left or not root_right:
                return False
            
            if root_left.val!=root_right.val:
                return False

            inner = helper(root_left.right, root_right.left)
            outer = helper(root_left.left, root_right.right)

            return inner and outer

        return helper(root, root)




        