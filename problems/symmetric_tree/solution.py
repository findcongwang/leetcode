# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.checkMirrored(root.left, root.right)
        
    
    def checkMirrored(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 and node2:
            if node1.val != node2.val:
                return False
            return self.checkMirrored(node1.left, node2.right) and self.checkMirrored(node1.right, node2.left)
        else:
            return False
    