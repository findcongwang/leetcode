from collections import Counter

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # each senator just ban the next opposing senator
        # update new senate each round
        
        banned = {"R": 0, "D": 0}
        next_senate = ""
        
        def other_side(s):
            return "R" if s == "D" else "D"
        
        while senate != len(senate) * senate[0]:
            # print(senate, banned)
            
            for s in senate:
                if banned[s] > 0:
                    banned[s] -= 1
                else:
                    next_senate += s
                    banned[other_side(s)] += 1
            senate = next_senate
            next_senate = ""
            
            
    
        if senate[0] == "R":
            return "Radiant"
        else:
            return "Dire"
        