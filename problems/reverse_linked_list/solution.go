/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {

    curr := head
    var top *ListNode = nil
    
    for curr != nil {
        temp := curr.Next
        curr.Next = top
        top = curr
        curr = temp        
    }
    
    return top
}