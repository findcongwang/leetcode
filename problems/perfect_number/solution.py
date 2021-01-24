import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return sum(self.divisorGenerator(num)) == 2*num
        
    def divisorGenerator(self, n):
        large_divisors = []
        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                yield i
                if i*i != n:
                    large_divisors.append(n / i)
        for divisor in reversed(large_divisors):
            yield divisor