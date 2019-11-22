func findDiagonalOrder(matrix [][]int) []int {
    // diagonals are for r in rows, r--,c++ until either out of bound
    // if r odd, append reversed
    
    output := []int{}
    
    if len(matrix) == 0 {
        return output
    }
    
    // go down left
    for r := 0; r < len(matrix); r++ {
        
        // fmt.Println("output", output)
        
        diag := []int{}
        
        // if r is odd, append to front (reversed)
        for tr, c := r, 0; tr >= 0 && c <= len(matrix[0])-1; tr, c = tr-1, c+1 {
            
            // fmt.Println("tr, c", tr, c)
            
            if r % 2 == 0 {
                diag = append(diag, matrix[tr][c])
            } else {
                diag = append([]int{matrix[tr][c]}, diag...)
            }
       
        }
        
        // fmt.Println("diag", diag)
        
        output = append(output, diag...)
    }
    
    // go across bottom
    for c := 1; c < len(matrix[0]); c++ {
        
        // fmt.Println("output", output)
        
        diag := []int{}
        
        // if h-1+c is odd, append to front (reversed)
        for r, tc := len(matrix)-1, c; r >= 0 && tc <= len(matrix[0])-1; r, tc = r-1, tc+1 {
            
            parity := len(matrix)-1+c
            // fmt.Println("r, tc", r, tc, "index -> ", parity, "val", matrix[r][tc])
            
            if parity % 2 == 0 {
                diag = append(diag, matrix[r][tc])
            } else {
                diag = append([]int{matrix[r][tc]}, diag...)
            }
       
        }
        
        // fmt.Println("diag", diag)
        
        output = append(output, diag...)
    }
    
    return output
}