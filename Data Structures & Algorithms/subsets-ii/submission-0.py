class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(curr, start):
            res.append(curr[:])

            for i in range(start, len(nums)):
                    if start < i and nums[i] == nums[i-1]:
                        continue
                    curr.append(nums[i])
                    backtrack(curr, i + 1)
                    curr.pop()
        backtrack([], 0)
        return res


        