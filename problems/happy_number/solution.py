class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(x) for x in str(n)]
        memset = set()
        
        while True:            
            n = sum([d**2 for d in digits])
            if n == 1:
                return True
            elif n in memset:
                return False
            else:
                memset.add(n)
                
            digits = [int(x) for x in str(n)]
