class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        # do I just brute force? what are recurrence?
        # f(1) is f(0) - n * array[-1] + sum[array[:-1]]
        n = len(A)
        asum = sum(A)
        fsum = sum([i*val for i, val in zip(range(n), A)])
        fmax = fsum
        
        for shift in range(n-1, -1, -1):
            # new sum is f(k-1) - n*array[shift] + sum(everything else)
            fsum = fsum + asum - (n * A[shift])
            fmax = max(fmax, fsum)
        
        return fmax