class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted([str(n) for n in range(1, n+1)])

            
            