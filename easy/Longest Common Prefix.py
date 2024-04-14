# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ''
        f_word = strs[0]

        pointer = 0
        while pointer < len(f_word):
            letter = f_word[pointer]
            for word in strs[1:]:
                if pointer>len(word)-1 or word[pointer]!=letter:
                    return ans
            ans+=f_word[pointer]
            pointer+=1
        return ans