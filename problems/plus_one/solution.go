func plusOne(digits []int) []int {
    
    newDigit := false
    digits[len(digits)-1] = digits[len(digits)-1] + 1
    
    // resolve carry
    for i := len(digits)-1; i >= 0; i-- {
        if digits[i] > 9 {
            if i == 0 { 
                newDigit = true 
            } else {
                digits[i-1] = digits[i-1] + 1   // carry
            }
            digits[i] = 0
        }
    }
    
    if newDigit {
        return append([]int{1}, digits...)
    }
    return digits
}