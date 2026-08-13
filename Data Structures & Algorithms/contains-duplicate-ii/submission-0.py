from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        items = defaultdict(int)
        for i in  range(len(nums)):
            if nums[i] in items:
                if i- items[nums[i]] <=k:
                    return True
            items[nums[i]] = i
        return False
            
        
        
        
        