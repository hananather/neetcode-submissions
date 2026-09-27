class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        res = 0
        for num in s:
            l = 1
            temp = num
            if temp - 1 in s:
                continue # skip this (wasted computation)
            while (temp + 1) in s:
                temp += 1
                l += 1
            res = max(res, l)
        return res