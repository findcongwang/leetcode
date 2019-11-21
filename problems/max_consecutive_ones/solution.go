func findMaxConsecutiveOnes(nums []int) int {
    max := 0
    start := -1
    
    // two pointers to find consec 1s, tracking max found so far
    for i := 0; i < len(nums); i++ {
        if nums[i] == 1 {
            if start == -1 { start = i }
        } else {
            start = -1
        }
        
        if start != -1 && (i-start+1) > max { max = i-start+1 }
        
        fmt.Printf("max so far: %d | start: %d, i: %d\n", max, start, i)
    }
    
    return max
}