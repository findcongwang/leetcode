class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
    
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                if i < len(nums)-2:
                    if nums[i] > nums[i+2]:
                        nums[i] = nums[i+1]
                    else:
                        nums[i+1] = nums[i]
                else:
                    nums[i+1] = nums[i]
                break

        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return False

        return True