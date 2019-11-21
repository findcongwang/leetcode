import "sort"

func arrayPairSum(nums []int) int {
    sort.Ints(nums)
    output := 0
    for i := 0; i < len(nums); i = i+2 {
        output += nums[i]
    }
    return output
}