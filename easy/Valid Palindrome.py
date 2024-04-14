# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        while l<r:
            while not s[l].isalpha() and not s[l].isdigit() and l < len(s):
                l+=1
                if l>r:
                    return True
            while not s[r].isalpha() and not s[r].isdigit() and r >= 1:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True