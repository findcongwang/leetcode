func dominantIndex(nums []int) int {
    
    if len(nums) == 0 { return -1 }

    max := nums[0]
    maxIndex := 0
    secondMax := 0
    
    for i, v := range(nums) {
        fmt.Printf("max: %d, maxIndex: %d, secondMax: %d\n", max, maxIndex, secondMax)
        
        if v > max {
            secondMax = max
            max = v
            maxIndex = i
        } else if v > secondMax && v != max {
            secondMax = v
        }
    }
    
    fmt.Println("---")
    fmt.Printf("max: %d, maxIndex: %d, secondMax: %d\n", max, maxIndex, secondMax)
    
    if max >= secondMax + secondMax {
        return maxIndex
    } else {
        return -1
    }
}