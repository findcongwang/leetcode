# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def leafHelper(node, target):
            if node is None:
                return None
            
            # process children first
            if node.left:
                node.left = leafHelper(node.left, target)
            if node.right:
                node.right = leafHelper(node.right, target)
            
            # then self
            if node.left is None and node.right is None and node.val == target:
                return None
            else:
                return node
            
        return leafHelper(root, target)