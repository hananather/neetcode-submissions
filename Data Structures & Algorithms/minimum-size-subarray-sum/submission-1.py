class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        ans = float('inf') # need to initalize
        curr = 0

        for R in range(len(nums)):
            curr += nums[R]
            while curr >= target:
                ans = min(ans, R - L + 1)
                curr -= nums[L]
                L +=1
        return 0 if ans == float('inf') else ans



        