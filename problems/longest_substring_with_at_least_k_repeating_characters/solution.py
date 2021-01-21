from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        # two passes, first to get the list of chars that occur >= k times
        # second pass to check if substring only contains valid chars
        counter = Counter(s)
        self.bannedChars = { c for c, n in counter.items() if n < k }
        if not self.bannedChars:
            return len(s)
        
        self.res = 0
        for num in range(1, len(counter) - len(self.bannedChars) + 1):
            self.solve(num, s, k)
        return self.res
        
    def solve(self, num, s, k):
        left,right = 0, 0
        match = 0
        count = 0
        d = dict()
        while right < len(s):
            if s[right] not in d:
                count += 1
                d[s[right]] = 1
            else:
                d[s[right]] += 1
            if d[s[right]] == k:
                match += 1
            while left < right and (count > num or s[left] in self.bannedChars):
                d[s[left]] -= 1
                if d[s[left]] == k-1:
                    match -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                    count -= 1
                left += 1
            if match == count == num:
                self.res = max(self.res, right-left+1)
            right += 1
            