import math

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        return self.primeFactors(num) - set([2,3,5]) == set()
    
    def primeFactors(self, n): 
        f = set()
        # 2 as a factor
        while n % 2 == 0: 
            f.add(2)
            n = n / 2
        # odd factors
        for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i == 0: 
                f.add(i)
                n = n / i 
        # if n is prime
        if n > 2: 
            f.add(n)
        return f