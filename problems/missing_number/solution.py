class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum 1..n is (n*(n+1))/2
        listsum = sum(nums)
        n = len(nums)
        return int((n*(n+1))/2) - listsum