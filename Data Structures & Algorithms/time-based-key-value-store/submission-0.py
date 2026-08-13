from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # need to find the right most value

        l, r = 0, len(self.values[key])

        while l < r:
            mid = (r + l) // 2
            if self.values[key][mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid
        
        if l == 0:
            return ""
        return self.values[key][l-1][1] 
    
                

        
