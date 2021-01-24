class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        res = []
        prevStart = nums[0]
        runLength = 0
        
        for n in nums[1:]:
            if n == prevStart + runLength + 1:
                runLength += 1
            else:
                if runLength == 0:
                    res.append(str(prevStart))
                else:
                    res.append("{}->{}".format(prevStart, prevStart + runLength))
                prevStart = n
                runLength = 0
        
        if runLength == 0:
            res.append(str(prevStart))
        else:
            res.append("{}->{}".format(prevStart, prevStart + runLength))
        
        return res