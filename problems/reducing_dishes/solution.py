import bisect

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # hunch: sorting dishes, if sorted list[0] is >= 0, all dishes shall be included
        # find out which negative dish to start on
        # for every neg dish we add:
        ## cost: the negative entry, benifit is sum of the of array to the right
        
        satisfaction.sort()
        idx = bisect.bisect_left(satisfaction, 0)
        
        # print(satisfaction, idx)
 
        # no positive dishes
        if idx >= len(satisfaction)-1:
            return 0
        
        while idx >= 0 and abs(satisfaction[idx]) < sum(satisfaction[idx+1:]):
            # print("good CBA", abs(satisfaction[idx]), "<", sum(satisfaction[idx+1:]))
            idx -= 1
        
        idx += 1
        print("endidx", idx)
        
        dishes = satisfaction[idx:]
        return sum([d*(idx+1) for idx, d in enumerate(dishes)])
