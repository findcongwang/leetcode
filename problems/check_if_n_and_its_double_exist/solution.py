class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = dict()
        for i in range(len(arr)):
            d[arr[i]]  = i
        
        for i in range(len(arr)):
            if arr[i]*2 in d and d[arr[i]*2] != i:
                return True
        return False
        