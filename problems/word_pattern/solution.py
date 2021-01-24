class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(pattern) != len(arr):
            return False
        
        d = dict()
        for i in range(len(pattern)):
            if pattern[i] in d and d[pattern[i]] != arr[i]:
                return False
            if pattern[i] not in d and arr[i] in d.values():
                return False
            d[pattern[i]] = arr[i]
            
        return True