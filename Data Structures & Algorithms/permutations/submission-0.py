class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(curr):

            if len(curr) == len(nums):
                results.append(curr.copy())
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
        backtrack([])
        return results
        