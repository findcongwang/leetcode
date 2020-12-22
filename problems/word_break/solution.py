from collections import deque

class Solution:
    def __init__(self):
        self.cache = {}
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True
        
        if s in self.cache:
            return self.cache[s]
        
        for w in wordDict:
            if s.startswith(w):
                self.cache[s] = self.wordBreak(s[len(w):], wordDict)
                if self.cache[s]:
                    return True

        self.cache[s] = False # carry over mem
        return self.cache[s]
