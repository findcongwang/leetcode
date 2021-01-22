# trade runtime for space? one pass to find idx, then random a idx

from collections import defaultdict
from random import randint

class Solution:
    def __init__(self, nums: List[int]):
        self._dict = defaultdict(list)
        for i in range(len(nums)):
            self._dict[nums[i]].append(i)

    def pick(self, target: int) -> int:
        i = randint(0, len(self._dict[target])-1)
        return self._dict[target][i]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)