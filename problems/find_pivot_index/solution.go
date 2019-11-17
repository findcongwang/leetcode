func pivotIndex(nums []int) int {
    if len(nums) == 0 {
        return -1
    } else if len(nums) == 1 {
        return 0
    }
    
    sums := make([]int, len(nums)+1)
    sums[0] = 0
    
    for i, v := range(nums) {
        if i == 0 {
            sums[i+1] = nums[i]
        } else {
            sums[i+1] = sums[i] + v
        }
    }
    
    fmt.Println(sums)
    
    for i, v := range(nums) {
       
        fmt.Printf("i = %d, left sum: %d, right sum: %d\n", i, sums[i], sums[len(nums)] - sums[i] - v)
        
        if sums[i] == sums[len(nums)] - sums[i] - v {
            return i
        }
    }
    
    return -1
}