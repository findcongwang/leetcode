class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xpow, ypow = [], []
        
        i, j = 0, 0
        if x != 1:
            while x**i <= bound:
                xpow.append(x**i)
                i += 1
        else:
            xpow = [1]
            
        if y != 1:
            while y**j <= bound:
                ypow.append(y**j)
                j += 1
        else:
            ypow = [1]
            
        return {
            xval + yval
            for xval in xpow
            for yval in ypow
            if xval + yval <= bound
        }
        