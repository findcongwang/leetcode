class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            # n is "at" the n-1th idx
            nums[abs(n)-1] = -abs(nums[abs(n)-1])
        
        res = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                res.append(idx+1)
                
        return res