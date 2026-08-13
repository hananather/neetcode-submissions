class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # treat this as dp
        # what is the state? 
        # state = subarray? this can be represented by i
        def dp(i):
            if i == 0:
                return nums[0]

            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + dp(i-1), nums[i])
            return memo[i]
        memo = {}
        res = float('-inf') 
        for i in range(len(nums)):
            res = max(res, dp(i))
        return res


