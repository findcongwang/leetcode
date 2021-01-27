class Solution:
    def divisorGame(self, N: int) -> bool:
        # try to find an recurrence
        # dp[i] is True if win on this move
        if N <= 1: return False
        
        dp = [None] * (N+1)
        dp[0] = False
        dp[1] = False
        dp[2] = True
        
        for i in range(3, N+1):            
            dp[i] = False
            for j in range(1, i):
                if i % j == 0 and not dp[i-j]:
                    dp[i] = True
                    break        
        return dp[N]
