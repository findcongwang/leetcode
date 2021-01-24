class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(nums), len(nums[0])
        if r * c != n * m:
            return nums
        
        res = [[0] * c for _ in range(r)]
        for i in range(n):
            for j in range(m):
                idx = i*m + j
                row = idx // c
                col = idx % c
                
                # print(idx, row, col)
                
                res[row][col] = nums[i][j]
                
        return res