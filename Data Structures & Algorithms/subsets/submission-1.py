class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(curr, k):
            # always start by appending a new subset to res
            res.append(curr[:])

            for i in range(k, len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        backtrack([],0)
        return res