type Coord struct {
    r int
    c int
}

func spiralOrder(matrix [][]int) []int {
    // start with r,c = 0,0 and
    // iterate over column until visited or out of bounds
    // iterate over row, repeat
    // clockwise so, right -> down -> left -> up
    
    output := []int{}
    
    if(len(matrix) == 0) {
        return output
    }
    
    m := len(matrix)
    n := len(matrix[0])
    
    visited := map[Coord]bool{}
    
    direction := "right"
    curr := Coord{}
    next := Coord{}
    
    // terminate when every cell is visited
    for len(visited) < m * n {
        
        fmt.Println(direction)
        
        // keep going on one direction until out of bound or visited
        for !outOfBounds(next,m,n) && !visited[next] {
            
            fmt.Println(next)
            
            output = append(output, matrix[next.r][next.c])
            visited[next] = true
            curr = next
            next = nextCoord(curr, direction)
            
            fmt.Println(output)
        }
        
        // change direction
        switch direction {
            case "right": direction = "down"
            case "down": direction = "left"
            case "left": direction = "up"
            case "up": direction = "right"
            default: fmt.Println("What?!")
        }
        
        next = nextCoord(curr, direction)
    }
    
    return output
}

func nextCoord(curr Coord, direction string) Coord {
    switch direction {
        case "right": return Coord{curr.r, curr.c+1}
        case "down": return Coord{curr.r+1, curr.c}
        case "left": return Coord{curr.r, curr.c-1}
        case "up": return Coord{curr.r-1, curr.c}
        default: return curr
    }   
}

func outOfBounds(pos Coord, numRows int, numCols int) bool {
    return (pos.r < 0 || pos.r >= numRows) || (pos.c < 0 || pos.c >= numCols)
}
