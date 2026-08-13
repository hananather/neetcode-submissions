class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(r, c):
            if r == m-1 and c == n-1:
                return 1
            if r == m or c ==n:
                return 0
            if r in memo and c in memo[r]:
                return memo[r][c]
            memo[r][c]  = dp(r +1, c) + dp(r, c+1)
            return memo[r][c]
        memo = defaultdict(dict)
        return dp(0,0)
        
        