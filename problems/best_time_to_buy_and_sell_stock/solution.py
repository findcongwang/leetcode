class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minCost[i] is the minimum price we could buy stock before on the ith day
        minCost = [float('inf')] * len(prices)
        for i in range(1, len(prices)):
            minCost[i] = min(minCost[i-1], prices[i-1])
        
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minCost[i])
        
        return maxProfit