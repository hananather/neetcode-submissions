class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            # cost of the ith
            # 2-ways to get to the ith step
            memo[i] = min(dp(i-1) + cost[i], dp(i-2) + cost[i])
            
            return memo[i]
        memo = {}
        return min(dp(len(cost) -1), dp(len(cost) - 2))
            

        