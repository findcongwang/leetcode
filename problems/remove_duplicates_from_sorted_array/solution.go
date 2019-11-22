func removeDuplicates(nums []int) int {
    exists := map[int]bool{}
    newlen := 0
    
    for i := 0; i < len(nums); i++ {
        if !exists[nums[i]] {
            exists[nums[i]] = true
            nums[newlen] = nums[i]
            newlen++
        }
    }
    
    return newlen
}