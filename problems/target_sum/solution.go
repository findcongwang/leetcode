func findTargetSumWays(nums []int, S int) int {
    return dfs(nums, S, 0)
}

func dfs(nums []int, S int, partial int) int {
    if len(nums) == 0 {
        if partial == S {
            return 1
        } else {
            return 0
        }
    } else {
        return dfs(nums[1:], S, partial + nums[0]) + dfs(nums[1:], S, partial - nums[0])
    }
}