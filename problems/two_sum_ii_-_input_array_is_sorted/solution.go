func twoSum(numbers []int, target int) []int {
    
    hash := map[int]int{}       // stores prev index
    
    for i := 0; i < len(numbers); i++ {
        fmt.Println(hash)
        
        if hash[numbers[i]] != 0 {            
            return []int{hash[numbers[i]], i+1}
        }
        hash[target-numbers[i]] = i+1
    }
    
    return []int{}
}