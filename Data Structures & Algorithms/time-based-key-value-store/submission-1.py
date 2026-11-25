class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.times.get(key) is not None:
            self.times[key].append([timestamp, value])
        else:
            self.times[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        # binary-search
        # Returns most recently saved timestamp <= timestamp
        if self.times.get(key) is None or len(self.times[key]) == 0:
            return ""
        
        timestamps = self.times[key]
        l, r = 0, len(timestamps) - 1
        highest = 0
        while l <= r:
            mid = (l+r) // 2
            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            if timestamps[mid][0] < timestamp:
                highest = timestamps[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return highest if highest != 0 else ""



# "foo" → [(1,"bar"), (4,"bar2"), (10,"bar3")]
# get(foo, 6)


# [1,4,10,20], 6 | return 1