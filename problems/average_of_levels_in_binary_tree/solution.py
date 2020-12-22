from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # queue for bfs, keep node and their level
        queue = deque([(root, 0)])
        
        # stats to keep (sum, count)
        stats = []
        
        while len(queue) > 0:
            node, h = queue.popleft()
            
            if node is None:
                continue
            
            if len(stats) < h+1:
                stats.append((0,0))
            
            s, c = stats[h]
            stats[h] = (s + node.val, c+1)
            
            queue.append((node.left, h+1))
            queue.append((node.right, h+1))
        
        return [
            s / c
            for s, c in stats
        ]