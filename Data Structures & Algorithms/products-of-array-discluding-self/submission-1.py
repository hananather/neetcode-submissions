class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I have never had to deal with consdiering the size of integers..
        # but I won't let this limitation hold me back lets continue..
        # the really dumb way to do this is via 2 nested for loops 
        # but this will result in O(n^2) time
        # lets start with this to warm up 
        prod = []
        for i in range(len(nums)):
            cur_prod = 1
            for j in range(len(nums)): 
                if i!=j:
                    cur_prod *= nums[j]
            prod.append(cur_prod)
        return prod

        

