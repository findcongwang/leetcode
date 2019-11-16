func canVisitAllRooms(rooms [][]int) bool {
    // make a queue of all visitable rooms, end when no more visitable room, keeping track of visited
    // count visisted same len as rooms
    
    if len(rooms) == 0 {
        return true
    }
    
    queue := []int{}
    visited := map[int]bool{}
    
    queue = append(queue, rooms[0]...)
    visited[0] = true
    
    for len(queue) > 0 {
        
        fmt.Println(queue)
        
        room := queue[0]
        queue = queue[1:]
        
        if !visited[room] {
            queue = append(queue, rooms[room]...)      // load the keys
            visited[room] = true
        }
    }
    
    fmt.Println("visited:", visited)
    return len(rooms) == len(visited)
}