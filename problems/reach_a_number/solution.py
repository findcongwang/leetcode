class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)
        i, count = 0, 0

        # get to the target
        while(i < target):
            count += 1
            i = i+count
            
        if(target == i):
            return count
        
        # adjust steps
        else:
            delta = abs(i-target)
            
            # while diff is odd
            while(delta % 2 != 0):
                count += 1
                i = i+count
                delta = abs(i-target)
            return count