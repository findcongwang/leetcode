/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

import "fmt"

func inorderTraversal(root *TreeNode) []int {
    var output []int
    
    if root == nil {
        return output
    }
    
    // make a stack to hold nodes
    var stack []*TreeNode
    
    visited := map[*TreeNode]bool{}
    stack = append(stack, root)
        
    for len(stack) > 0 {        
        node := stack[len(stack)-1]
        
        // go down left whenever possible
        if node.Left != nil && !visited[node.Left] {
            stack = append(stack, node.Left)
            continue
        } else {
            if !visited[node] {
                output = append(output, node.Val)
                visited[node] = true
            }           
            if node.Right != nil && !visited[node.Right] {
                stack = append(stack, node.Right)
                continue
            }
        }
        stack = stack[:len(stack)-1]        // pop from top
    }
    
    return output
}