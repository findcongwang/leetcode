class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # count occurances using a set
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        
        return list(s)