class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr, start, r):
            if r == 0:
                res.append(curr[:])
            
            for i in range(start, len(nums)):
                num = nums[i]
                if r - num >= 0:
                    curr.append(num)
                    backtrack(curr, i, r - num)
                    curr.pop()
        backtrack([],0, target)
        return res



        