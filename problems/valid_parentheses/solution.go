import "fmt"

func isValid(s string) bool {
    // stack left brackets, pop as right bracket shows up
    
    var stack []rune
    
    for _, c := range s {       
        switch c {
        case '(':
            stack = append(stack, c)
        case '{':
            stack = append(stack, c)
        case '[':
            stack = append(stack, c)
        case ')':
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
                return false
            } else {
                stack = stack[:len(stack)-1]
            }
        case '}':
            if len(stack) == 0 || stack[len(stack)-1] != '{' {
                return false
            } else {
                stack = stack[:len(stack)-1]
            }
        case ']':
            if len(stack) == 0 || stack[len(stack)-1] != '[' {
                return false
            } else {
                stack = stack[:len(stack)-1]
            }
        }
    }
    
    return len(stack) == 0
}