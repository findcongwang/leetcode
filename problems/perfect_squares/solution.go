import "fmt"
import "math"

type Node struct {
    sum int     // running sum
    val int     // node value
    dist int
}

func numSquares(n int) int {
    // build a list of possible values, which are squares of [1 .. floor(sqrt(n))]
    // least number used is found via BFS since each level represents additional count
    
    // TLE, need to optimize with bilateral BFS, default is sum up, queueNeg on remainder
    
    var queue []Node
    visited := map[int]int{}
    
    var queueNeg []Node
    visitedNeg := map[int]int{}
    
    initVals := getPerfectSquaresDesc(n)
    for _, initVal := range(initVals) {
        queue = append(queue, Node{initVal, initVal, 1})
        visited[initVal] = 1
        
        queueNeg = append(queueNeg, Node{n - initVal, initVal, 1})
        visitedNeg[n - initVal] = 1
    }
    
    for len(queue) > 0 && len(queueNeg) > 0 {
        // sum up BFS
        node := queue[0]
        queue = queue[1:]       // dequeue
        
        if node.sum == n {
            return node.dist
        } else if visitedNeg[node.sum] != 0 {
            fmt.Printf("pos %v found %d(%d) in neg\n", node, node.sum, visitedNeg[node.sum])
            return node.dist + visitedNeg[node.sum]
        } else {
            nbrVals := getPerfectSquaresDesc(n - node.val)
            for _, nbrVal := range nbrVals {
                newSum := node.sum + nbrVal
                if newSum <= n && visited[newSum] == 0 {
                    queue = append(queue, Node{newSum, nbrVal, node.dist + 1})
                    visited[newSum] = node.dist + 1
                }
            }
        }
        
        fmt.Println("Pos BTS")
        fmt.Println(queue)
        fmt.Println(visited)
        
        // countdown BFS
        nodeNeg := queueNeg[0]
        queueNeg = queueNeg[1:]     // dequeue
        
        if nodeNeg.sum == 0 {       // note: neg queue uses node.sum as remainder
            return node.dist
        } else if visited[nodeNeg.sum] != 0 {
            fmt.Printf("neg %v found %d(%d) in pos \n", nodeNeg, nodeNeg.sum, visited[nodeNeg.sum])
            return nodeNeg.dist + visited[nodeNeg.sum]
        } else {
            nbrVals := getPerfectSquaresDesc(nodeNeg.val)
            for _, nbrVal := range nbrVals {
                newRem := nodeNeg.sum - nbrVal
                if newRem >= 0 && visitedNeg[newRem] == 0 {
                    queueNeg = append(queueNeg, Node{newRem, nbrVal, nodeNeg.dist + 1})
                    visitedNeg[newRem] = nodeNeg.dist + 1
                }
            }
        }
        
        fmt.Println("Neg BTS")
        fmt.Println(queueNeg)
        fmt.Println(visitedNeg)
    }
        
    // technically should never reach for positive n
    return -1
}

// return perfect squares
func getPerfectSquaresDesc(rem int) []int {    
    m := int(math.Floor(math.Sqrt(float64(rem))))
    var ps []int
    for i := m; i > 0; i-- {
        ps = append(ps, int(math.Pow(float64(i), 2)))
    }
    return ps
}