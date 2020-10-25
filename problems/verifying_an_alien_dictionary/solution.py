class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        htable = {x: idx for idx, x in enumerate(order)}
       
        for w1, w2 in zip(words, words[1:]):
            for idx, l in enumerate(w1):
                
                if len(w2) <= idx or htable[l] > htable[w2[idx]]:
                    return False
                
                elif htable[l] < htable[w2[idx]]:
                    break
            
        return True
        