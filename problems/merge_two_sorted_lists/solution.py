# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        
        if (l1 and not l2) or (l1 and l2 and l1.val < l2.val):
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        cur = head
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        
        return head
                