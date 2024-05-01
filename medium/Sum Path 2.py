# Given the root of a binary tree and an integer targetSum,
# return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return 
        
        ans = []

        def dfs(node, target, path):
            target = target+node.val
            path.append(node.val)
            if target==targetSum and not node.right and not node.left:
                ans.append(path[:])
                path.pop()
                return 
            elif not node.right and not node.left:
                path.pop()
                return 
            else:
                if node.left: dfs(node.left, target, path)
                if node.right: dfs(node.right, target, path)
                path.pop()
                return
        
        dfs(root, 0, [])
        return ans