class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        
        k = 3
        while k < n+1:
            for j in range(1, k):
                dp[k] = max(dp[k], dp[k-j]*j, (k-j)*j)
            k += 1
        
        # print(dp)
        return dp[-1]