# store culminative sum, then return culsum j - i?

from itertools import accumulate

class NumArray:
    def __init__(self, nums: List[int]):
        self.culsum = list(accumulate(nums))

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.culsum[j]
        return self.culsum[j] - self.culsum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)