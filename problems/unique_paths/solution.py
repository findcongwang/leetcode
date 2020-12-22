class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dynamic programming approach
        # each cell can be moved from top or left, so M(i,j) = M(i-1,j) + M(i, j-1)
        # M(0,0) is zero, but irrelevant
        
        dp=[[None for _ in range(n)] for _ in range(m)]
        
        for i in range(0,n):
            dp[0][i] = 1
        for j in range(0,m):
            dp[j][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]