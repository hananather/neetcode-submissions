import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        top_k = []
        heapq.heapify(top_k)
        for key, val in counts.items():
            heapq.heappush(top_k, (val, key))
            if len(top_k) > k:
                heapq.heappop(top_k)
        return [key for _, key in top_k]

        