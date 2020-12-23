class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        # sum of the whole array is 3k where k is the target sum
        # use cululative sum and check if k, 2k and 3k are in the list
        # check that csum[-1] is 3k
        
        csum = [A[0]] * len(A)
        for i in range(1, len(A)):
            csum[i] = csum[i-1] + A[i]
        
        if csum[-1] % 3 != 0:
            return False
        
        k = int(csum[-1] / 3)
        
        # print(csum, k)
        
        try:
            idx_k = csum.index(k)
            idx_2k = csum.index(2*k, idx_k+1)
            return idx_2k < len(csum)-1
            
        except ValueError:
            return False
