class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        
        # dp[r][c] = max size of square that can be completed with m[r][c]
        dp = [[0] * m for _ in range(n)]
        dp[0] = matrix[0]
        for r in range(n):
            dp[r][0] = matrix[r][0]
        
        # either you use [r][c] or you don't 
        # if m[r][c] is zero, dp[r][c] is zero
        # otherwise, dp[r][c] is the min of top, topleft, left, plus 1
        for r in range(1, n):
            for c in range(1,m):
                if matrix[r][c] == 0:
                    dp[r][c] = 0
                else:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1
        
        return sum([sum(row) for row in dp])