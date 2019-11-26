import "sort"

type triplet struct {
    a int
    b int
    c int
}

func threeSum(nums []int) [][]int {
    mem := map[int]int{}
    
    solHash := map[triplet]bool{}
    solutions := [][]int{}
    
    // hash all numbers, index+1 to avoid 0 index
    for i := 0; i < len(nums); i++ {
        mem[nums[i]] = i+1
    }
    
    // n^2 loops to find sums that equal to -(nums[i]+nums[j])
    for i := 0; i < len(nums); i++ {
        for j := i+1; j < len(nums); j++ {          
            if mem[-(nums[i]+nums[j])] != 0 && 
                mem[-(nums[i]+nums[j])] != i+1 && 
                mem[-(nums[i]+nums[j])] != j+1 {
                    
                    // fmt.Println(solHash)
                
                    vals := []int{-(nums[i]+nums[j]), nums[i], nums[j]}
                    sort.Ints(vals)
                    if !solHash[triplet{vals[0], vals[1], vals[2]}] {
                        solutions = append(solutions, vals)
                        solHash[triplet{vals[0], vals[1], vals[2]}] = true
                    }
            }
        }
    }
    
    return solutions
}