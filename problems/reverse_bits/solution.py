class Solution:
    def reverseBits(self, n: int) -> int:
        count = 31
        num = 0
        while n > 0:
            num = num + ((n&1) * 2**count)
            n = n >> 1
            count -= 1
        return num