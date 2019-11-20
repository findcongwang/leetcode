func strStr(haystack string, needle string) int {
    
    if len(needle) == 0 {
        return 0
    }
    
    for i := 0; i < len(haystack); i++ {
        if len(haystack)-i < len(needle) {
            return -1       // no space for substring
        }
        
        slice := haystack[i:i+len(needle)]
        fmt.Println(slice)
        
        if slice == needle {
            return i
        }
    }
    
    return -1
}