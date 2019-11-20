func longestCommonPrefix(strs []string) string {
    // can start from any string since we're looking for the common prefix
    
    if len(strs) == 0 {
        return ""
    }
    
    result := ""
    
    for i := 0; i < len(strs[0]); i++ {
        for _, str := range(strs) {
            if i > len(str)-1 || strs[0][i] != str[i] {
                return result
            }
        }
        result += string(strs[0][i])
    }
    
    return result
}