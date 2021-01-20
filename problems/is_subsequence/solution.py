class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointers on both strings
        i, j = 0, 0
        while i < len(t):
            if j == len(s):
                return True
            
            if t[i] == s[j]:
                j += 1
            
            i += 1
        
        return j == len(s)