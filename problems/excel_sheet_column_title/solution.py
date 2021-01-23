class Solution:
    def convertToTitle(self, n: int) -> str:
        name = ""
        while n != 0:
            name = self.decToAlpha((n-1) % 26) + name
            n = (n-1) // 26
        return name
    
    def decToAlpha(self, n):
        return chr(ord("A") + n)