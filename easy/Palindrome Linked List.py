# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Find the middle of the LList
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of LList
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Compare the first half to the second one:
        f_part_head = head
        s_part_head = prev
        while s_part_head:
            if f_part_head.val!=s_part_head.val:
                return False
            f_part_head = f_part_head.next
            s_part_head = s_part_head.next
        return True
        