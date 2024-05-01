# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack:
                if t>stack[-1][1]:
                    ans[stack[-1][0]]=i-stack[-1][0]
                    stack.pop()
                else:
                    break
            stack.append((i, t))
        return ans