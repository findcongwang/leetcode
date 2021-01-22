class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        for i in range(len(xstr)//2):
            if xstr[i] != xstr[-(i+1)]:
                return False
        return True
            