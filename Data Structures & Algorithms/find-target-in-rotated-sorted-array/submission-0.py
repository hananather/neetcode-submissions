class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2 

            if nums[mid] == target:
                return mid
            elif nums[low]  <= nums[mid]:
                # check if target
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else: # this statement only executes if first part is not sorted
                if nums[mid] <= target <=nums[high]: 
                    low = mid + 1 # should this be in an if block?
                else:
                    high = mid - 1
                
        return -1 




