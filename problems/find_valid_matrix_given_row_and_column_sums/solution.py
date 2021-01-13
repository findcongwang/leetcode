class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0] * len(colSum) for _ in range(len(rowSum))]
        while sum(rowSum) + sum(colSum) != 0:
            minRowIdx = self.getMinIdx(rowSum)
            minColIdx = self.getMinIdx(colSum)
            
            val = min(rowSum[minRowIdx], colSum[minColIdx])
            result[minRowIdx][minColIdx] = val
            rowSum[minRowIdx] -= val
            colSum[minColIdx] -= val
            
            # print(rowSum, colSum)
        # for line in result:
        #     print(line)
        return result
        
    
    # return minIdx that is not zero or None if all zer0es
    def getMinIdx(self, arr):
        minVal, minValIdx = float("inf"), None
        for i in range(len(arr)):
            if arr[i] != 0 and arr[i] < minVal:
                minVal = arr[i]
                minValIdx = i
        return minValIdx
        