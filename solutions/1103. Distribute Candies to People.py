class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        idx = 0
        num_gift = 1
        result = [0] * num_people
        
        while candies > 0:
            idx = idx % num_people
            result[idx] += min(num_gift, candies)
            candies -= num_gift
            num_gift += 1
            idx += 1
        
        return result
​
