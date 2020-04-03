class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # build an array of max sums of prev subarrays
        max_array = []
        
        for idx, n in enumerate(nums):
            if idx == 0:
                max_array.append(n)
            else:
                max_array.append(max(max_array[idx-1] + n, n))
            
        print(max_array)
        return max(max_array)