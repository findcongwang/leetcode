class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # if empty, return false
        # check the first int by bits, then check the len of data to the number of 1s found until first zero
        if len(data) < 1:
            return True
        
        data = [str(bin(n))[2:].zfill(8) for n in data]
        refIdx = 0
        validUTF = True
        
        while refIdx < len(data):
            # find length of current char
            idx = data[refIdx].find("0")

            # print(data, refIdx, idx)
            
            # if this implies invalid 1-4 byte char
            if idx < 0 or idx > 4:
                return False
            
            # if single byte char
            if idx == 0:
                if data[refIdx][0] != "0":
                    return False
                refIdx += 1
            if idx == 1:
                return False
            else:
                # there must be idx-1 continuation bytes, which must start with 10----
                for i in range(1, idx):
                    if refIdx+i >= len(data) or data[refIdx+i][:2] != "10":
                        return False

                # check next char
                refIdx += idx
    
        return True
