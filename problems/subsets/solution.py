from itertools import combinations, chain

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = chain.from_iterable([combinations(nums, i) for i in range(len(nums)+1)])
        return list(powerset)
