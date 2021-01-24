# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = None
        node = None
        
        while l1 or l2:
            part = carry
            if l1:
                part += l1.val
                l1 = l1.next
            if l2:
                part += l2.val
                l2 = l2.next
            
            if not node:
                result = ListNode(part % 10)
                node = result
            else:
                node.next = ListNode(part % 10)
                node = node.next
            carry = part // 10
            
        if carry != 0:
            node.next = ListNode(carry)

        return result