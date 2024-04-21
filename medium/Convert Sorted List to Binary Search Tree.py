from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def search_mid(head):
            curr_slow = head
            curr_fast = head
            prev = None
            while curr_fast and curr_fast.next:
                curr_fast = curr_fast.next.next
                prev = curr_slow
                curr_slow = curr_slow.next
            if prev:
                prev.next=None
            return curr_slow

        if not head:
            return None
        
        mid = search_mid(head)
        
        root = TreeNode(mid.val)
        
        if head.val == mid.val:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
    
        return root
        