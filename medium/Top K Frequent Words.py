# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest.
# Sort the words with the same frequency by their lexicographical order.

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        ans = []
        for key, _ in sorted(d.items(), key=lambda x: (-x[1], x[0])):
            if len(ans)<k:
                ans.append(key)
            else:
                break
        return ans