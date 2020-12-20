import math
import numpy

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # straight forward n log n, sort and trim and get avg
        p = math.floor(len(arr) * 0.05)
        return numpy.mean(sorted(arr)[p:len(arr)-p])
        