class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # using long division logic, hash store the idx of the start of the subsequence
        # (quotient, remainder): idx
        d = dict()
        
        negative = (numerator < 0) ^ (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # check if no decimals, base case
        res = str(numerator // denominator)
        remainder = numerator % denominator
        
        if remainder == 0:
            return self.sign(res, negative)
        res += "."
        
        # stop long division when no more remainder, or if a repeat is found
        while remainder*10 % denominator != 0:
            # print(d, remainder)
            quotient = remainder*10 // denominator
            newRemainder = remainder*10 % denominator
            
            if (quotient, newRemainder) in d:
                # then from d[(quotient, newRemainder)] to end is a repeating subsequence
                idx = d[(quotient, newRemainder)]
                seq = res[idx:]
                res = res[:idx] + "({})".format(seq)
                return self.sign(res, negative)
            
            d[(quotient, newRemainder)] = len(res)
            res += str(quotient)
            remainder = remainder*10 % denominator
        
        
        res += str(remainder*10 // denominator)
        return self.sign(res, negative)

    def sign(self, strInt, negative=False):
        if strInt == "0":
            return "0"
        if negative:
            return "-" + strInt 
        return strInt
    