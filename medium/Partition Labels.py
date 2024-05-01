# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result