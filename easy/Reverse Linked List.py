# Given the head of a singly linked list, reverse the list, and return the reversed list.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            nxt_node = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_node
        return prev

        