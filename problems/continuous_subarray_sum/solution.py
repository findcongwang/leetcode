from itertools import accumulate

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # culsum, then csum[j] - csum[i-1] is sum from i to j
        # check for all i,j s.t. i<j if sum % k is zero?
        if len(nums) <= 1:
            return False
        
        csum = list(accumulate(nums))
        # print(csum)
        
        for j in range(1,len(nums)):
            # where i == 0
            if self.modKZero(csum[j], k):
                return True
            
            for i in range(1,j):
                segsum = csum[j] - csum[i-1]
                if self.modKZero(segsum, k):
                    return True
        return False
    
    def modKZero(self, n, k):
        if k == 0:
            return n == 0
        return n % k == 0