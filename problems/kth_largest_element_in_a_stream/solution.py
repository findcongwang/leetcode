import heapq

# keep two heaps, min-heap of the largest k elements, and max-heap of remainders

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._topk = nums
        self._vals = []
        self._k = k
        heapq.heapify(self._topk)
        
        while len(self._topk) > k:
            # keeps negated values for maxheap
            heapq.heappush(self._vals, -heapq.heappop(self._topk))
        
#         print("_topk", self._topk)
#         print("_vals", self._vals)
        
        
    def add(self, val: int) -> int:
        if len(self._topk) < self._k:
            heapq.heappush(self._topk, val)
        
        # does not affect topk
        elif val < self._topk[0]:
            heapq.heappush(self._vals, -val)
        else:
            kp1 = heapq.heapreplace(self._topk, val)    
            heapq.heappush(self._vals, -kp1)        
        
        # print("_topk", self._topk)
        # print("_vals", self._vals)
        
        return self._topk[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)