from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        
        counter = Counter(deck)
        freqs = list(counter.values())
        
        if len(freqs) == 1:
            return True
        
        if len(freqs) == 2:
            if self.gcd(freqs[0], freqs[1]) != 1:
                return True
            else:
                return False
        else:
            gcd = self.gcd(freqs[0], freqs[1])
            for i in range(2, len(freqs)):
                gcd = self.gcd(gcd, freqs[i])
            if gcd != 1:
                return True
            else:
                return False
    
    def gcd(self, x, y):
        if x < y:
            x, y = y, x
        while y != 0:
            x, y = y, x % y
        return x