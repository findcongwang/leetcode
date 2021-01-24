class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] <= arr[0]:
            return False
        
        desc = False
        for i in range(1, len(arr)):
            # check increasing
            if not desc and arr[i-1] >= arr[i]:
                desc = True
            # check descreasing
            if desc and arr[i-1] <= arr[i]:
                return False
        
        # check one peak
        return desc
