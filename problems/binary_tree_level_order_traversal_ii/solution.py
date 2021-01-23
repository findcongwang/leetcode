# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        queue = deque([(root, 0)])
        
        while queue:
            node, depth = queue.popleft()
            if node is None:
                continue
                
            if depth >= len(levels):
                levels.append([node.val])
            else:
                levels[depth].append(node.val)
            
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        
        return list(reversed(levels))