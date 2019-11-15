import ( 
    "fmt"
    "strings"
    "strconv"
) 

type Item struct {
    t string        // number, operator, or string
    val string
}

func decodeString(s string) string {
    // use a stack to match #[*], generates output when ']' is encountered
    var stack []Item
    stack = append(stack, Item{"string", ""})
    
    for _, c := range s {
        
        fmt.Println(stack)
        
        if c >= '0' && c <= '9' {
            // append to top k literal or add new one
            if stack[len(stack)-1].t == "number" {
                stack[len(stack)-1].val = stack[len(stack)-1].val + string(c)
            } else {
                stack = append(stack, Item{"number", string(c)})
            }
        } else if c == '[' {
            // pattern starts
            stack = append(stack, Item{"operator", string(c)})
        } else if c == ']' {
            // resolve repeition, merge string down
            // pop string, pop [, pop number, add expanded pattern to next item
            str := stack[len(stack)-1].val
            num := stack[len(stack)-3].val
            stack = stack[:len(stack)-3]    // remove k[a-Z*
            if k, err := strconv.Atoi(num); err == nil {
                if stack[len(stack)-1].t == "string" {
                    stack[len(stack)-1].val = stack[len(stack)-1].val + strings.Repeat(str, k)
                } else {
                    stack = append(stack, Item{"string", strings.Repeat(str, k)})
                }
                
            } else {
                fmt.Printf("Error: k: %s was not a valid number.", num)
            }
        } else {
            // must be a char, since input is always valid
            if stack[len(stack)-1].t == "string" {
                stack[len(stack)-1].val = stack[len(stack)-1].val + string(c)
            } else {
                // note: top must have been '['
                stack = append(stack, Item{"string", string(c)})
            }
        }
    }
    
    return stack[0].val
}