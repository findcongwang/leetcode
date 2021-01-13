class Solution:
    def lastRemaining(self, n: int) -> int:
        # on the kth op, the step is 2^k
        # array is [start:end:step]
        # on left passes, start += step
        # on right passes, end -= step 
        
        if n == 1:
            return 1
        
        k = 0
        start, end = 1, n
        
        while start < end:
            # print(start, end)
            
            step = 2**k
            
            # if list is odd, both start and end shrinks in
            if (n // step) % 2 != 0:
                start += step
                end -= step
                
            # if k is even, going from left
            elif k % 2 == 0:
                start += step
                
            # going from right
            else:
                end -= step
            k += 1
        
        # print(start, end)
        return start