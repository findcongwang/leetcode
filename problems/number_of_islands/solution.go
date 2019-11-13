type Node struct {
    r int
    c int
}

func numIslands(grid [][]byte) int {
    num := 0
    if len(grid) == 0 {
        return 0
    }
    h := len(grid)
    w := len(grid[0])
    
    // each cell is checked once, init a visited table
    visited := make([][]uint, h)
    for r := range visited {
        visited[r] = make([]uint, w)
	}
    
    // check every cell to increment num
    for r, row := range grid {
        for c, val := range row {
            fmt.Printf("%d, %d:\n", r, c)
            
            if val == '0' || visited[r][c] == 1 {
                // if water or visited, skip
                continue
            } else {
                // if land (val == 1), do BFS and mark connected nodes as visited, resulting in one island
                var queue []Node
                queue = append(queue, Node{r, c})
                visited[r][c] = 1

                // explore this new island
                for len(queue) > 0 {                 
                    node := queue[0]
                    queue = queue[1:]   // dequeue
                    
                    fmt.Printf("current (%d, %d): ", node.r, node.c)
                    
                    if node.c > 0 && visited[node.r][node.c-1] == 0 && grid[node.r][node.c-1] != '0' {
                        // add left neighbour if not out of bounds, not visited, and not water
                        visited[node.r][node.c-1] = 1
                        queue = append(queue, Node{node.r, node.c-1})
                        
                        fmt.Printf("added left (%d, %d)=%c ", node.r, node.c-1, grid[node.r][node.c-1])
                    }
                    if node.c < w-1 && visited[node.r][node.c+1] == 0 && grid[node.r][node.c+1] != '0' {
                        // add right neighbour if not out of bounds, not visited, and not water
                        visited[node.r][node.c+1] = 1
                        queue = append(queue, Node{node.r, node.c+1})
                        
                        fmt.Printf("added right (%d, %d)=%c ", node.r, node.c+1, grid[node.r][node.c+1])
                    }
                    if node.r > 0 && visited[node.r-1][node.c] == 0 && grid[node.r-1][node.c] != '0' {
                        // add top neighbour if not out of bounds, not visited, and not water
                        visited[node.r-1][node.c] = 1
                        queue = append(queue, Node{node.r-1, node.c})
                        
                        fmt.Printf("added top (%d, %d)=%c ", node.r-1, node.c, grid[node.r-1][node.c])
                    }
                    if node.r < h-1 && visited[node.r+1][node.c] == 0 && grid[node.r+1][node.c] != '0' {
                        // add down neighbour if not out of bounds, not visited, and not water
                        visited[node.r+1][node.c] = 1
                        queue = append(queue, Node{node.r+1, node.c})
                        
                        fmt.Printf("added down (%d, %d)=%c ", node.r+1, node.c, grid[node.r+1][node.c])
                    }
                    
                    fmt.Println(queue)
                }
                num = num + 1   // finished exploring one island
            }
            
            // fmt.Println(visited)
        }
    }
    
    return num
}