class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        prime = [True for i in range(n)] 
        prime[0] = False
        prime[1] = False
        
        p = 2
        while p*p < n:
            if prime[p]:
                # update all multiples of p 
                for i in range(p*2, n, p):
                    prime[i] = False
            p += 1
        
        return prime.count(True)