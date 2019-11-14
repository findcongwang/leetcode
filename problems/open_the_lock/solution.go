import "fmt"

type Node struct {
    code string
    dist int
}

func openLock(deadends []string, target string) int {
    // a node e.g. "0000" is connected to 8 nodes, e.g. "1000", "9000", "0100" ...
    // since all distances are 1, the shortest can be found with BFS
    // keep visited node with distances and do bidirectional to boost runtime
    
    var queueFromStart []Node
    var visitedFromStart []Node
    queueFromStart = append(queueFromStart, Node{"0000", 0})
    visitedFromStart = append(visitedFromStart, Node{"0000", 0})
    
    var queueFromEnd []Node
    var visitedFromEnd []Node
    queueFromEnd = append(queueFromEnd, Node{target, 0})
    visitedFromEnd = append(visitedFromEnd, Node{target, 0})
    
    for len(queueFromStart) > 0 || len(queueFromEnd) > 0 {
        if len(queueFromStart) == 0 || len(queueFromEnd) == 0 {
            return -1
        }
        
        // iterate start -> end search
        qsNode := queueFromStart[0]
        queueFromStart = queueFromStart[1:]  // dequeue

        if (qsNode.code == target) {
            return qsNode.dist
        }
        if index := findCode(visitedFromEnd, qsNode.code); index != -1 {
            // combine search results when bridged
            fmt.Printf("start side found %v, [s%d, e%d]\n", 
                       qsNode, qsNode.dist, visitedFromEnd[index].dist)
            fmt.Println(visitedFromStart)
            fmt.Println(visitedFromEnd)
            return qsNode.dist + visitedFromEnd[index].dist
        }
        if contains(deadends, qsNode.code) {
            continue        // path terminates on deadends
        }
        for _, ncode := range neighbours(qsNode.code) {
            if findCode(visitedFromStart, ncode) == -1 {
                queueFromStart = append(queueFromStart, Node{ncode, qsNode.dist + 1})
                visitedFromStart = append(visitedFromStart, Node{ncode, qsNode.dist + 1})
            }
        }
        
        // iterate start <- end search
        qeNode := queueFromEnd[0]
        queueFromEnd = queueFromEnd[1:]     // dequeue

        if (qeNode.code == "0000") {
            return qeNode.dist
        }
        if index := findCode(visitedFromStart, qeNode.code); index != -1 {
            // combine search results when bridged
            fmt.Printf("end side found %v, [s%d, e%d]\n", 
                       qeNode, qeNode.dist, visitedFromStart[index].dist)
            fmt.Println(visitedFromStart)
            fmt.Println(visitedFromEnd)
            return qeNode.dist + visitedFromStart[index].dist
        }
        if contains(deadends, qeNode.code) {
            continue        // path terminates on deadends
        }
        for _, ncode := range neighbours(qeNode.code) {
            if findCode(visitedFromEnd, ncode) == -1 {
                queueFromEnd = append(queueFromEnd, Node{ncode, qeNode.dist + 1})
                visitedFromEnd = append(visitedFromEnd, Node{ncode, qeNode.dist + 1})
            }
        }
    }
    
    // if all paths results to deadends, return -1
    return -1
}

func pmod(x, d int) int {  
    r := x % d
    if r < 0 {
        return r + d
    } else {
        return r
    }
}

func neighbours(code string) []string {
    var nbs []string
    for i := range code {
        // add +/- 1 of the index, keep the rest
        d := int(code[i] - '0')
        nbs = append(nbs, fmt.Sprintf("%s%d%s", code[:i], pmod((d-1), 10), code[i+1:]))
        nbs = append(nbs, fmt.Sprintf("%s%d%s", code[:i], pmod((d+1), 10), code[i+1:]))
    }
    return nbs
}

func findCode(arr []Node, str string) int {
   for index, a := range arr {
      if a.code == str {
         return index
      }
   }
   return -1
}

func contains(arr []string, str string) bool {
   for _, a := range arr {
      if a == str {
         return true
      }
   }
   return false
}