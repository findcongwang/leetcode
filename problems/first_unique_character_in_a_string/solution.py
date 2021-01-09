class Solution:
    def firstUniqChar(self, s: str) -> int:
        dups = set()
        seen = set()
        for c in s:
            if c in seen:
                dups.add(c)
            else:
                seen.add(c)
        
        for i in range(len(s)):
            if s[i] not in dups:
                return i
        
        return -1