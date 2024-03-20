# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a certain timestamp.


from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append((timestamp, value))


    def bin_search(self, timestamps, timestamp):
        if not timestamps:
            return None

        l, r = 0, len(timestamps)-1
        while l<=r:
            mid = l+(r-l)//2
            if timestamp==timestamps[mid][0]:
                return mid
            elif timestamp>timestamps[mid][0]:
                l = mid + 1
            else:
                r = mid -1
        return r if r>=0 else -1


    def get(self, key, timestamp):
        if key not in self.data:
            return ""
        
        timestamps = self.data[key]
        index = self.bin_search(timestamps, timestamp)
        
        if index >= 0:
            return timestamps[index][1]
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)