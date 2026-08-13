class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr, k):
            # always start by appending a new subset to res
            res.append(curr[:])

            for i in range(k, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        backtrack([],0)
        return res