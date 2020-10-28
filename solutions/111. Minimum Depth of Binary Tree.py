# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.minDepthHelper(root, 1)
    
    def minDepthHelper(self, node, depth):
        if node.left is None and node.right is None:
            return depth
        elif node.left is None:
            return self.minDepthHelper(node.right, depth+1)
        elif node.right is None:
            return self.minDepthHelper(node.left, depth+1)
        else:
            return min(self.minDepthHelper(node.left, depth+1), self.minDepthHelper(node.right, depth+1))
