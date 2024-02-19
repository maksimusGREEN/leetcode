# Given the heads of two singly linked-lists headA and headB,
# return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None
        
        currA, currB = headA, headB
        
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
            
        return currA
        