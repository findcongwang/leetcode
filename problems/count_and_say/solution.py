class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        if n == 1:
            return res
        
        for _ in range(n-1):
            res = self.sayNext(res)
        return res
    
    
    def sayNext(self, s):       
        res = ""
        prev = s[0]
        count = 1
        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                res += str(count) + str(prev)
                count = 1
                prev = c
        
        if count > 0:
            res += str(count) + str(prev)
        return res