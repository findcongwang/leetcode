class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mem = set()
        for n in nums:
            if n in mem:
                mem.remove(n)
            else:
                mem.add(n)
        return mem.pop()