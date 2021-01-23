class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
            
        # two pointers, skip non alphanumerics
        i, j = 0, len(s)-1
        
        while i < len(s) and not s[i].isalnum():
            i += 1
        while j >= 0 and not s[j].isalnum():
            j -= 1
        
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            while not s[i].isalnum():
                i += 1
            while not s[j].isalnum():
                j -= 1
        
        return True