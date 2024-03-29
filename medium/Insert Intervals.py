# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = newInterval

        inserted = False

        result = []

        for interval in intervals:
            if interval[1]<start:
                result.append(interval)
            elif interval[0]>end:
                if not inserted:
                    result.append([start, end])
                    inserted = True
                result.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
            
        if not inserted:
            result.append([start, end])
  
        return result

print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))