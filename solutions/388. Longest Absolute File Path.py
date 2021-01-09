class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
​
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # use Node with val referrencing their abs path length
        # keep track of longest so far
        root = Node("")
        maxPathLength = 0
        maxPathNode = root
        prevNodes = {0: root}  # map of depth -> Node
        
        for line in input.split("\n"):
            # each line is a new Node, denoted by len
            # if number of \ts are more than prev line, then its a new children
            # otherwise less, its the prev Node at that depth (num of \ts are the depth)
            depth = line.count("\t") + 1            # +1 to account for root
            
            parent = prevNodes[depth-1]
            newNode = Node(parent.val + "/" + line[(depth-1):])
            parent.children.append(newNode)
            prevNodes[depth] = newNode
            
            # if is a file and longer abs path
            if "." in line[(depth-1):] and len(newNode.val)-1 > maxPathLength:
                maxPathLength = len(newNode.val)-1
                maxPathNode = newNode
        
        print(maxPathNode.val)
        return maxPathLength
