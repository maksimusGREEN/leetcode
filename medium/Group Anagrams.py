
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            key = ''.join(sorted(s))
            ans.setdefault(key, []).append(s)
        return list(ans.values())
        

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))