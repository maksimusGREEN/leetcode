# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height)-1
        max_volume = 0
        while lp<rp:
            wide = rp-lp
            max_volume = max(max_volume, min(height[lp], height[rp])*wide)
            if height[lp]>height[rp]:
                rp-=1
            else:
                lp+=1
        return max_volume