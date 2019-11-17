func search(nums []int, target int) int {
    return searchHelper(nums, target, 0)
}

// return index of target if found, or -1
func searchHelper(num []int, target int, baseIndex int) int {
    
    fmt.Println(baseIndex, num)
    
    if len(num) <= 2 {
        if len(num) > 0 && num[0] == target { 
            return baseIndex 
        } else if len(num) > 1 && num[1] == target { 
            return baseIndex + 1 
        } else {
            return -1
        }
    } else {
        pivot := int(len(num) / 2.0)
        if num[pivot] > target {    // search left
            return searchHelper(num[0:pivot], target, baseIndex)
        } else if num[pivot] < target {  // search right
            return searchHelper(num[pivot:], target, baseIndex + pivot)
        } else {
            // found on pivot
            return baseIndex + pivot
        }
    }
}