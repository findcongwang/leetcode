from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = Counter()
        count = 0
        for i in range(len(nums)):
            if nums[i] in h:
                count += h[nums[i]]
            h[nums[i]] += 1
        return count
