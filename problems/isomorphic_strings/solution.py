class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = dict()
        mapped = set()
        for i in range(len(s)):            
            if s[i] in d and d[s[i]] != t[i]:
                return False
            if s[i] not in d and t[i] in mapped:
                return False
            
            d[s[i]] = t[i]
            mapped.add(t[i])
        
        return True
    