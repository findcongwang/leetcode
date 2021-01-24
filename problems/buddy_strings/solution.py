from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False
        
        counter = Counter(A)
        diffs = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diffs.append(i)
            
        if len(diffs) == 2 and A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]]:
            return True
        if len(diffs) == 0 and counter.most_common(1)[0][1] > 1:
            return True
        
        return False