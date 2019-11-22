func moveZeroes(nums []int)  {
    
    
    index := 0
    numZeroes := 0
    
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[index] = nums[i]
            index++
        } else {
            numZeroes++
        }
    }

    for z := 0; z < numZeroes; z++ {
        nums[len(nums)-1-z] = 0
    }
}