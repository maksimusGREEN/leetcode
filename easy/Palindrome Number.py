# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        revX = 0
        inputNum=x

        while x>0:
            revX = revX*10 + x%10
            x=x//10
        return revX==inputNum
       