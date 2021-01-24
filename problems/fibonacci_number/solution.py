class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        lastEven, lastOdd = 0, 1
        for k in range(2, n):
            if k % 2 == 0:
                lastEven = lastEven + lastOdd
            else:
                lastOdd = lastEven + lastOdd
        
        return lastEven + lastOdd