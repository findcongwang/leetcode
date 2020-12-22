class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # i - K <= r <= i + K, j - K <= c <= j + K where (r, c) is a valid position
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = sum(
                    mat[r][c]
                    for r in range(max(0, i-K), min(m, i+K+1))
                    for c in range(max(0, j-K), min(n, j+K+1))
                )
                
        return ans