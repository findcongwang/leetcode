func mySqrt(x int) int {
    // Initial Condition: left = 0, right = length-1
    // Termination: left > right
    // Searching Left: right = mid-1
    // Searching Right: left = mid+1
    
    if x < 2 { return x }
    
    left, right := 0, x
    
    for left <= right {
        mid := (right-left) / 2
        
        fmt.Println("mid", left+mid)
        
        if checkSqrt(left+mid, x) { 
            return left+mid 
        } else if (left+mid)*(left+mid) > x {
            // go left
            right = left+mid-1
        } else {
            left = left+mid+1
        }
    }
    
    return left
}

func checkSqrt(x int, t int) bool {
    if x*x == t { return true }
    
    prod := int64(x+1)*int64(x+1)
    return x*x < t && prod > int64(t)
}
