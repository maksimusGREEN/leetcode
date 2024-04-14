# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        cnt = 0
        is_single_letter = False

        for l in s:
            d[l]+=1

        for k in d:
            if d[k]%2==0:
                cnt+=d[k]
            else:
                cnt+=d[k]-1
                is_single_letter=True
        return cnt if not is_single_letter else cnt+1
