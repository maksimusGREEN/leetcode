# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        ans = []

        if not digits:
            return []

        def dfs(i, comb):

            if i==len(digits):
                ans.append(comb)
                return

            for l in d[digits[i]]:
                dfs(i+1, comb+l)

        dfs(0, '')

        return ans



        