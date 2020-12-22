class Solution:
    def longestWord(self, words: List[str]) -> str:
        # sort the list and track via set, keeping only longest seen so far
        words.sort()
        s = set()
        res, maxL = words[0], 1
        
        # print(words)
        
        for w in words:
            if len(w) == 1:
                s.add(w)
            else:
                if w[:-1] in s:
                    s.add(w)
                    
                    if len(w) > maxL:
                        res, maxL = w, len(w)
        
            # print(res, maxL)
        
        return res
