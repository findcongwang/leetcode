# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root
        queue = deque([(root, None)])
        while queue:
            node, parent = queue.popleft()
            if node is None:
                continue
            
            if parent is None:
                node.val = 0
            elif node == parent.left:
                node.val = parent.val * 2 + 1
            elif node == parent.right:
                node.val = parent.val * 2 + 2
            else:
                raise ValueError()
            
            queue.append((node.left, node))
            queue.append((node.right, node))

    def find(self, target: int) -> bool:
        # bfs, when target < node.val, end search
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node is None or node.val > target:
                continue
            if node.val == target:
                return True
            queue.append(node.left)
            queue.append(node.right)

        return False
            
            
            
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)