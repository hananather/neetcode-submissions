class Solution:
    def rob(self, nums: List[int]) -> int:
        # tabuluar approach
        # state_i = maximum money upto  house_i 
        # what is the maxmum we can rob if we only consider i houses
        # key insight = max amount up to ith house is a function of max_(i-1) and max_(i-2)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * (len(nums) + 1)
        dp[0], dp[1]= nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[len(nums) -1]
        