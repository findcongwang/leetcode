# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        if root is None:
            return self.res
        
        self.pathHelper(root, [])
        return self.res
    
    def pathHelper(self, node, path):
        if node.left is None and node.right is None:
            path.append(str(node.val))
            self.res.append("->".join(path))
            return
        
        if node.left:
            self.pathHelper(node.left, path[:] + [str(node.val)])
        if node.right:
            self.pathHelper(node.right, path[:] + [str(node.val)])
        