import "math"

func reverseString(s []byte) []byte {
    mid := int(math.Floor(float64(len(s)) / 2.0))
    
    fmt.Println(len(s), mid)
    
    for i := 0; i < mid; i++ {
        // swap s[i] with s[-i]
        temp := s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = temp
    }
    
    return s
}