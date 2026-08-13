class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * len(nums)*2
        for i in range(len(nums)):
            out[i] = nums[i]
            out[i+n] = nums[i]
        return out
        