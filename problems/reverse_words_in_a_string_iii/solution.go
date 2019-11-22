func reverseWords(s string) string {
    result := ""
    word := []byte{}

    for p2 := 0; p2 < len(s); p2++ {
        if s[p2] != ' ' {
            word = append([]byte{s[p2]}, word...)
        } else {
            if len(word) != 0 {
                result = result + string(word) 
                word = []byte{}
            }
            result = result + string(s[p2])
        }
    }
    
    if len(word) != 0 {
        result = result + string(word)
    }
    
    return result
}