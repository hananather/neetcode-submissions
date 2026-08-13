import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-s for s in stones]
        heapq.heapify(s)
        
        # at each iteration we destory a stone
        while s and len(s) > 1:
            x = heapq.heappop(s)
            y = heapq.heappop(s)
            if x - y == 0:
                continue
            heapq.heappush(s, x - y)
        if s:
            return -s[0]
        return 0
