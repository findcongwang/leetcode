"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        visited = {}
        
        def dfs(node):
            if node:
                if node in visited:
                    return visited[node]
                
                val = node.val
                new_node = Node(val=val)
                visited[node] = new_node
                
                neighbours = node.neighbors
                for n in neighbours:
                    new_n = dfs(n)
                    new_node.neighbors.append(new_n)
                
                return new_node
                
        return dfs(node)
