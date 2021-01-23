# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.mem = dict()
        if root is None:
            return True
        
        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)
        
        return (
            abs(leftH-rightH) <= 1 and
            self.isBalanced(root.left) and
            self.isBalanced(root.right)
        )
        
    def getHeight(self, node):
        if node in self.mem:
            return self.mem[node]
        if node is None:
            return 0
        
        h = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        self.mem[node] = h
        return h
        