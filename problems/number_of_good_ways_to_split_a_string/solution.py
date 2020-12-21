from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        # use Counter (rs) on the whole string one pass
        # then iterate and check counts with a ls Counter too
        rs = Counter(s)
        ls = Counter()
        good_splits = 0
        
        for c in s:
            ls[c] += 1
            rs[c] -= 1
            
            if rs[c] == 0:
                del rs[c]
            
            if len(ls.keys()) == len(rs.keys()):
                good_splits += 1
        
        return good_splits