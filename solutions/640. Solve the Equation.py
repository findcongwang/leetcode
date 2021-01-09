from collections import deque
import operator
​
​
class Solution:
    def solveEquation(self, equation: str) -> str:
        # parsing question. split into lhs and rhs from eq
        # move all x to lhs, all constants to rhs, then
                
        lhs, rhs = tuple(equation.split("="))
        ops = { "+": operator.add, "-": operator.sub }
        
        # to parse each side into (mut, const), or (a,b) for expression ax + b
        # assume valid input
        def parseExpr(expr):
            a, b = 0, 0
            stack = deque()
            
            # process from back, if operator, pop and resolve until empty
            for c in reversed("+" + expr):
                if c in ["+", "-"]:
                    # pop and resolve
                    num = ""
                    top = ""
                    while len(stack) > 0:
                        top = stack.pop()
                        if top.isdigit():
                            num += top
                    if top == "x":
                        a = ops[c](a, int(num) if num else 1)
                    else:
                        b = ops[c](b, int(num) if num else 0)
                else:
                    stack.append(c)    
            return (a, b)
        
        lhsa, lhsb = parseExpr(lhs)
        rhsa, rhsb = parseExpr(rhs)
        
        # reduce to a'x = b'        
        ap, bp = lhsa - rhsa, rhsb - lhsb
        
        if ap == bp == 0:
            return "Infinite solutions"
        elif ap == 0:
            return "No solution"
        else:
            bp = int(bp/ap)
            ap = ""
            
        return "{}x={}".format(ap, bp)
        
        
        
                    
                
        
        
