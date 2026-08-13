class Solution:
    def climbStairs(self, n: int) -> int:
        # add cache
        cache = {}
        if n == 0:
            return 1
        if n < 0: # negative
            return 0
        elif n in cache:
            return cache[n]
        cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        
        return cache[n]
        


        