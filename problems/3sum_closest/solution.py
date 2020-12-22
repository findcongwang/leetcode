class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort the array, then two pointers for closest sum
        nums.sort()
        closest = float("inf")
        
        for i in range(len(nums)):
            twosum = target - nums[i]
            j, k = i+1, len(nums)-1
            
            while j < k:
                currsum = nums[i] + nums[j] + nums[k]
                
                if abs(target - closest) > abs(target - currsum):
                    closest = currsum
                
                if nums[j] + nums[k] < twosum:
                    j += 1
                else:
                    k -= 1
            if closest == target:
                break
                
        return closest
                
        
        