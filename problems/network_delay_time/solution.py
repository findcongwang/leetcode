import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:        
        # bfs, track visited, keep track of longest travel time
        # tracks table for min time to each node
        
        unvisited = set(range(1,N+1))
        distances = {(i, j): v for i, j, v in times}
        
        pq = [(0, K)]
        dist = 0
                
        while len(pq) > 0:
            curr_dist, i = heapq.heappop(pq)
            
            if i in unvisited:
                unvisited.discard(i)
                dist = curr_dist
                
                for j in unvisited:
                    if (i, j) in distances:
                        heapq.heappush(pq, (curr_dist + distances[(i, j)], j))
        
                if not unvisited:
                    return dist
                
        return -1
        
            
