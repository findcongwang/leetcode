func generate(numRows int) [][]int {
    if numRows == 0 {
        return [][]int{}
    }
    
    prev := []int{1}
    output := [][]int{prev}
    
    
    for r := 1; r < numRows; r++ {
        newRow := nextRow(prev)
        output = append(output, newRow)
        prev = newRow
    }
    
    return output
}

func nextRow(prevRow []int) []int {
    nextRow := make([]int, len(prevRow)+1)
    nextRow[0] = 1
    nextRow[len(nextRow)-1] = 1
    for i := 1; i < len(prevRow); i++ {
        nextRow[i] = prevRow[i-1] + prevRow[i]
    }
    return nextRow
}