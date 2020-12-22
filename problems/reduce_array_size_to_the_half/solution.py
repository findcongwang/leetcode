from collections import Counter
import heapq
import math

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # problem sounds like removing a few most frequent numbers from array
        # then put frequency into max heap and extract until more than half is met
        
        freq = Counter(arr)
        
        target = math.floor(len(arr) / 2 + 0.5)    # ceil
        removed_num = 0
        removed_set = set()
        
        for k, f in freq.most_common():
            removed_num += f
            removed_set.add(k)
            
            if removed_num >= target:
                break
            
        return len(removed_set)

        