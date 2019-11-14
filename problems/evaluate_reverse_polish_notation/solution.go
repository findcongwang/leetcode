import (
    "fmt"
    "strconv"
)

func evalRPN(tokens []string) int {
    var operands []int
    
    // push non operands (integers) onto the stack, and pop -> put back result when operator
    
    for _, val := range tokens {
        switch val {
        case "*":
            oprd2 := operands[len(operands)-1]
            oprd1 := operands[len(operands)-2]
            operands = operands[:len(operands)-2]
            operands = append(operands, oprd1 * oprd2)
        case "/":
            oprd2 := operands[len(operands)-1]
            oprd1 := operands[len(operands)-2]
            operands = operands[:len(operands)-2]
            operands = append(operands, oprd1 / oprd2)
        case "+":
            oprd2 := operands[len(operands)-1]
            oprd1 := operands[len(operands)-2]
            operands = operands[:len(operands)-2]
            operands = append(operands, oprd1 + oprd2)
        case "-":
            oprd2 := operands[len(operands)-1]
            oprd1 := operands[len(operands)-2]
            operands = operands[:len(operands)-2]
            operands = append(operands, oprd1 - oprd2)
        default:
            if num, err := strconv.Atoi(val); err == nil {
                operands = append(operands, num)
            } else {
                return -1       // error and exit
            }
        }
    }
    
    return operands[0]
}