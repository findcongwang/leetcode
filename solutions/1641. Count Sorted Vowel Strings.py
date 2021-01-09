class Solution:
    def countVowelStrings(self, n: int) -> int:
        count = [1,1,1,1,1]
        for _ in range(1,n):
            for i in range(4,-1,-1):
                count[i] += sum(count[:i])
        return sum(count)
​
