class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # base cases
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            return n <= 1 and flowerbed[0] == 0
        
        print("before", flowerbed)
        
        # first
        if flowerbed[0] != 1 and flowerbed[1] != 1:
            n -= 1
            flowerbed[0] = 1
            
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] != 1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        
        # last
        if flowerbed[-1] != 1 and flowerbed[-2] != 1:
            n -= 1
            flowerbed[-1] = 1
        
        print("after", flowerbed)
        
        return n <= 0