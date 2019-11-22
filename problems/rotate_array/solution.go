func rotate(nums []int, k int) {
    // keep start (k) and shift elements to +k mod length until k is encountered
    
    k = k % len(nums)
    count := 0
    
    for start := 0; count < len(nums); start++ {
        current := start
        prev := nums[start]
        
        // cycle it
        for {
            next := (current + k) % len(nums)
            temp := nums[next]
            nums[next] = prev
            prev = temp
            current = next
            count ++
            
            if start == current {
                break
            }
        }
    }
}