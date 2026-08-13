class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def dp_max(i):
            if i == 0:
                return nums[0]
            
            if i in memo_max:
                return memo_max[i]
            memo_max[i] = max(nums[i]*dp_max(i-1), nums[i], dp_min(i-1)* nums[i])

            return memo_max[i]

        def dp_min(i):
            if i == 0:
                return nums[0]
            
            if i in memo_min:
                return memo_min[i]
            memo_min[i] = min(nums[i]*dp_max(i-1), nums[i], dp_min(i-1)* nums[i])

            return memo_min[i] 
        memo_max = {}
        memo_min = {}
        res = float('-inf')
        for i in range(len(nums)):
            res = max(res, dp_max(i))
        return res