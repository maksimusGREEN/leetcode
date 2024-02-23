# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(None)

        dummy.next = head

        # define len of linklist
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length+=1

        # Move pointer to target node
        cur = dummy
        s = 0
        while s<length-n:
            cur = cur.next
            s+=1
        
        # Remove target node
        cur.next = cur.next.next if cur.next.next else None
        return dummy.next
        
        