# Given a binary tree, determine if it is height-balanced


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            return max(getHeight(root.left), getHeight(root.right))+1 if root else 0

        if not root:
            return True

        lh, rh = getHeight(root.left), getHeight(root.right)

        if abs(lh-rh)>1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
