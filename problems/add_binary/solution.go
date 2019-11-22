func addBinary(a string, b string) string {
    result := ""
    carry := 0
    
    i, j := len(a)-1, len(b)-1
    
    for i >= 0 || j >= 0 {
        sum := carry
        if j >= 0 {
            sum += int(b[j] - '0')
            j--
        }
        if i >= 0 {
            sum += int(a[i] - '0')
            i--
        }
        result = string((sum % 2) + '0') + result
        carry = sum / 2
        
        fmt.Println("sum, carry", sum, carry)
    }
    
    if carry != 0 {
        result = string(carry + '0') + result
    }
    
    return result
}