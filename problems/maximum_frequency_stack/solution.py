# dont need a stack array
# need a freq counter
# need dict to map idxes
# almost pop the highest freq, idx, use max heap?

from collections import Counter
import heapq

class FreqStack:
    def __init__(self):
        self.len = 0
        self.heap = []
        self.freq = Counter()

    def push(self, x: int) -> None:
        self.freq[x] += 1
        heapq.heappush(self.heap, (-self.freq[x], -self.len, x))
        self.len += 1

    def pop(self) -> int:
        freq, idx, x = heapq.heappop(self.heap)
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()