type Item struct {
    temp int
    index int
}

func dailyTemperatures(T []int) []int {
    // build a stack of (temp, index)
    
    var stack []Item
    output := make([]int, len(T))
    
    for i, t := range T {          
        // today is warmer, struck out days from earlier and calculate days from i
        for len(stack) > 0 && t > stack[len(stack)-1].temp {
            output[stack[len(stack)-1].index] = i - stack[len(stack)-1].index
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, Item{t, i})   // add to the stack and keep going
    }
    
    // T ended, all remaining days are 0
    return output
}