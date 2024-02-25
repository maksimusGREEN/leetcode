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