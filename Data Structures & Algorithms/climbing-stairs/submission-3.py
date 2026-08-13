class Solution:
    def climbStairs(self, n: int) -> int:
        # add cache
        cache = {}
        def memo(cache, n):
            if n == 0:
                return 1
            if n < 0: # negative
                return 0
            elif n in cache:
                return cache[n]
            cache[n] = memo(cache, n-2) + memo(cache , n-1)
            
            return cache[n]
        return memo(cache, n)