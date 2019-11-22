import "math"

func minSubArrayLen(s int, nums []int) int {
    // two pointer one pass, track active sum
    
    minLen := math.MaxInt32
    
    activeSum := 0
    a := 0
    
    for b := 0; b < len(nums); b++ {
        activeSum += nums[b]
        
        for activeSum >= s {
            if (b-a+1) < minLen { minLen = b-a+1 }
            fmt.Println(a, b, activeSum, minLen)
            
            activeSum -= nums[a]
            a++
        }
    }
    
    if minLen == math.MaxInt32 { return 0 }
    return minLen
}