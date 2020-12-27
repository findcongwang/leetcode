import math
import numpy as np

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # brute force since the world is 50x50
        # use numpy to map out the matrix, then call np.max
        quality = np.zeros(shape=(51,51))
        
        # iterate over towers, and increment quality on affected nodes covered under area
        for tx, ty, tq in towers:
            # check all points in (tx-1) +- r and (ty-1) +- r
            minx, maxx = (max(-1, tx-1-radius), min(50, tx+radius))
            miny, maxy = (max(-1, ty-1-radius), min(50, ty+radius))
            
            for x in range(minx, maxx):
                for y in range(miny, maxy):
                    d = math.sqrt((x-tx+1)**2 + (y-ty+1)**2)
                    if d <= radius:
                        quality[x+1][y+1] += math.floor(tq / (1+d))

        print(quality.max())
        return np.unravel_index(quality.argmax(), quality.shape)