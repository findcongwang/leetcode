from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        
        # put values in a stack, 
        # if char, update top element if str, add the top element
        # if num, update top element if num, otherwise add num
        # if ], then pop and resolve until k
        # if [, ignore cuz input is valid
        stack = deque()
        
        for c in s:
            # print(stack)
            
            if len(stack) == 0:
                if c.isdigit():
                    stack.append(int(c))
                else:
                    stack.append(c)
            
            # push a divider
            elif c == "[":
                stack.append(None)
            
            # resolve the subsequence, k is stack [-3], divider is stack[-2], str is stack[-1]
            elif c == "]":
                pattern = stack.pop()
                _divider = stack.pop()
                k = stack.pop()
                subseq = pattern * k
                
                # merge back up
                while stack and isinstance(stack[-1], str):
                    prev = stack.pop()
                    subseq = prev + subseq
                
                stack.append(subseq)
                
            # if number
            elif c.isdigit():
                if isinstance(stack[-1], int):
                    stack[-1] = stack[-1] * 10 + int(c)
                else:
                    stack.append(int(c))
            
            # else, letter
            else:
                if isinstance(stack[-1], str):
                    stack[-1] += c
                else:
                    stack.append(c)
                    
        return "".join(stack)
                    