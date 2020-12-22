from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        max_area = 0
        
        def area_from_points(p1, p2, p3):
            one = p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]
            two = p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0]
            return abs(one-two)/2
        
        for p1, p2, p3 in combinations(points, 3):
            max_area = max(max_area, area_from_points(p1, p2, p3))
            
        return max_area
            