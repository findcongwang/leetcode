from itertools import combinations, chain

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        powerset = chain.from_iterable([combinations(nums, i) for i in range(len(nums)+1)])
        return list(set(powerset))