class Solution:   
    def isPathCrossing(self, path: str) -> bool:
        curr = [0, 0]
        visited = {0: set([0])}    # { x: set(y) }
    
        for step in path:
            if step == "N":
                curr[0] += 1
            elif step == "S":
                curr[0] -= 1
            elif step == "E":
                curr[1] += 1
            elif step == "W":
                curr[1] -= 1
            
            if curr[0] not in visited:
                visited[curr[0]] = set([curr[1]])
            elif curr[1] in visited[curr[0]]:
                return True
            else:
                visited[curr[0]].add(curr[1])
            
        return False
    