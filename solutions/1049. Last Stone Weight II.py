class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # every possible sum at n stones is all combinations of +/- at each previous entry
        # every additional number, the possible sum doubles
        # mem[n] is the results at n+1 stones
        mem = []
        
        for n in range(len(stones)):
            if n == 0:
                mem.append({-stones[0], stones[0]})
            else:
                mem.append(set())
                for prev_sum in mem[n-1]:
                    mem[n].add(prev_sum - stones[n])
                    mem[n].add(prev_sum + stones[n])
            
            # print(mem[n])
        
        return min([v for v in mem[-1] if v >= 0])
            
        
