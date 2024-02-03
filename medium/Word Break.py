# Given a string s and a dictionary of strings wordDict, return true if s can be
# segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache
        def helper(s):
            if not s:
                return True

            for word in wordDict:
                lw = len(word)
                if word==s[:lw]:
                    if helper(s[lw:]):
                        return True

            return False
        return helper(s)