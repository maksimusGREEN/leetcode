# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

class Solution:
    def isPalindrome(self, head):
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Compare the first half with the reversed second half
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True