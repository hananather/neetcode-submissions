class Solution:
    def climbStairs(self, n: int) -> int:
        # add cache
        cache = {}
        def memo(n):
            if n == 0:
                return 1
            if n < 0: # negative
                return 0
            elif n in cache:
                return cache[n]
            cache[n] = memo(n-2) + memo(n-1)
            
            return cache[n]
        return memo(n)