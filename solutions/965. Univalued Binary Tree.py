# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # dfs, check all val equal to root
        return self.isUnivalTreeHelper(root, root.val)
    
    def isUnivalTreeHelper(self, node, val):
        return (
            node.val == val
            and (node.left is None or self.isUnivalTreeHelper(node.left, val))
            and (node.right is None or self.isUnivalTreeHelper(node.right, val))
        )
​
