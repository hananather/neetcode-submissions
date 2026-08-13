class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # step 1 
        out = []
        nums = sorted(nums) 
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1] :
                # skip this value
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                value = nums[l] + nums[r] + val
                if value < 0:
                    l += 1
                elif value > 0:
                    r -= 1
                elif value == 0:
                    out.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l< r:
                        l +=1
               
        return out
        