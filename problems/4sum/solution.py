from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # split problem into two 2sum problems
        quads = set()
        pairSums = defaultdict(list)
        
        for i in range(1, len(nums)-1):
            # scan right to match quads
            for j in range(i+1, len(nums)):
                part = nums[i] + nums[j]
                diff = target - part
                if diff in pairSums:
                    for quad in [pair + [nums[i], nums[j]] for pair in pairSums[diff]]:
                        quads.add(tuple(sorted(quad)))
                            
            
            # scan left to add to hash
            for k in range(0, i):
                part = nums[k] + nums[i]
                pairSums[part].append([nums[k], nums[i]])
                
        return list(quads)
