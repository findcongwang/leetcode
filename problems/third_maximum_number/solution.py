import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        seen = set()
        
        for n in nums:
            if n in seen:
                continue
            
            seen.add(n)
            if len(heap) < 3:    
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)
            
        if len(heap) == 3:
            return heap[0]
        
        while heap:
            maxVal = heapq.heappop(heap)
        return maxVal
            