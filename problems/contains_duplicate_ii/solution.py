from collections import OrderedDict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2 or k == 0:
            return False
        
        cache = OrderedDict()
        
        for i in range(len(nums)):
            if nums[i] in cache:
                return True
            if len(cache) >= k:
                _ = cache.popitem(last=False)
            cache[nums[i]] = True
        
        return False
