func removeElement(nums []int, val int) int {
    // two pointer, a to point end of string, b to iterate
    
    strlen := 0
    
    for i:=0; i < len(nums); i++ {
        if(nums[i] != val) {
            nums[strlen] = nums[i]
            strlen++
        } else {
            nums[i] = 0
        }
    }
    
    return strlen
}