# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        freq_s = Counter(s[:len(p)-1])
        freq_p = Counter(p)

        result = []

        for i in range(len(p)-1, len(s)):
            freq_s[s[i]]+=1
            f_val_ind = i-len(p)+1
            if freq_s==freq_p:
                result.append(f_val_ind)
            freq_s[s[f_val_ind]] -=1
            if freq_s[s[f_val_ind]] == 0:
                del freq_s[s[f_val_ind]]
        
        return result