class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            if i <= 0:
                return float('inf')
            if i in memo:
                return memo[i]
            memo[i] = min(dp(i-j) for j in coins) + 1

            return memo[i]
        memo = {}
        res = dp(amount)
        return res if res != float('inf') else -1
