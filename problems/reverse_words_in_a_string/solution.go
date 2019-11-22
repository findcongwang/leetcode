func reverseWords(s string) string {
    // two pointer to detect word, push to front of result
    
    result := ""
    word := []byte{}

    for p2 := 0; p2 < len(s); p2++ {
        if s[p2] != ' ' {
            word = append(word, s[p2])
        } else {
            if len(word) != 0 {
                result = string(word) + " " + result
                word = []byte{}
            }
        }
    }
    
    if len(word) != 0 {
        result = string(word) + " " + result
    }
    
    if result == "" { return result }
    return result[:len(result)-1]
}
