from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # bfs, each subtree must be complete as well
        # compete if empty, both children are empty
        # only the last right most can have left child
        
        queue = deque()
        flag = False
        queue.append(root)
        
        while len(queue) > 0:
            node = queue.popleft()
            
            if node is None:
                continue
            
            if node.left:
                if flag == True:
                    return False
                queue.append(node.left)
            else:
                flag = True
                
            if node.right:
                if flag == True:
                    return False
                queue.append(node.right)
            else:
                flag = True
            
        return True
        
        
        
        