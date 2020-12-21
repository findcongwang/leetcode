# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque 

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        stack = deque()
        
        while head is not None:
            stack.append(head.val)
            head = head.next
        
        sum = 0
        digit = 0
        while len(stack) > 0:
            if stack.pop() == 1:
                sum += 2 ** digit
            digit += 1
        
        return sum