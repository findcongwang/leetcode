class Solution:
    def trailingZeroes(self, n: int) -> int:
        # number of 5s and 10s in the sequence
        res = 0
        while n // 5 != 0:
            res += n // 5
            n = n // 5
        return res
    