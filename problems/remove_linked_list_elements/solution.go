/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
    curr := head
    var prev *ListNode = nil
    
    for curr != nil {
        if curr.Val == val {
            if prev == nil {
                head = head.Next
            } else {
                prev.Next = curr.Next
            }
        } else {
            prev = curr    
        }
        curr = curr.Next
    }
    
    return head
}

    