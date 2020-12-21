class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # bruteforce is to setup all rectangles and compute area
        # need to find the furthest consective h and v cuts
        
        m = 1000000007
        
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_horz, max_vert = 0, 0
        h_i, v_i = 0, 0
        
        #print(horizontalCuts)
        #print(verticalCuts)
        
        for idx in range(1, len(horizontalCuts)):
            if horizontalCuts[idx] - horizontalCuts[idx-1] > max_horz:
                max_horz = horizontalCuts[idx] - horizontalCuts[idx-1]
                h_i = idx - 1
        
        for idx in range(1, len(verticalCuts)):
            if verticalCuts[idx] - verticalCuts[idx-1] > max_vert:
                max_vert = verticalCuts[idx] - verticalCuts[idx-1]
                v_i = idx - 1
        
        #print(max_horz, max_vert, h_i, v_i)
        
        return (max_horz % m) * (max_vert % m) % m
        