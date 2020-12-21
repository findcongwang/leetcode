class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ksum = sum(nums[:k])
        max_ksum = sum(nums[:k])
        
        print(ksum)
        
        for idx in range(k, len(nums)):
            ksum = ksum - nums[idx-k] + nums[idx]
            if ksum > max_ksum:
                max_ksum = ksum
            
#             print("+", nums[idx], "-", nums[idx-k])
#             print(max_ksum)
        
        return max_ksum / k
            
            
        