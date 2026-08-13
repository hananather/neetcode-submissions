class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) -1
        while low < high: # need to think about this condition 
            mid = (low + high) // 2 
            if nums[high] < nums[mid]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

        