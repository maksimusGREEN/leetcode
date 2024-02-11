# Given the head of a linked list, rotate the list to the right by k places.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k==0:
            return head
        
        n = 1 

        cur = head
        while cur.next:
            cur = cur.next
            n+=1
        
        cur.next = head
        
        k = k%n

        for _ in range(n-k-1):
            head = head.next

        new_head = head.next
        head.next = None

        return new_head


        


