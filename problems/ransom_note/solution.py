from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCounter = Counter(magazine)
        noteCounter = Counter(ransomNote)
        
        for noteKey in noteCounter:
            if magCounter[noteKey] < noteCounter[noteKey]:
                return False
        return True