class Solution:
    def integerReplacement(self, n: int) -> int:
        # DP instead of array use dict for mem
        mem = { 1: 0, 2: 1 }
        return self.dpHelper(n, mem)
        
    def dpHelper(self, n, mem):
        if n in mem:
            return mem[n]
        
        if n % 2 == 0:
            mem[n] = self.dpHelper(n//2, mem) + 1
            return mem[n]
        
        else:
            mem[n] = min(self.dpHelper((n-1)//2, mem), self.dpHelper((n+1)//2, mem)) + 2
            return mem[n]
        