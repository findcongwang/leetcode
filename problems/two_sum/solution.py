class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pass
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for j in range(len(nums)):
            part = target - nums[j]
            if part in d and d[part] != j :
                return [d[part], j]