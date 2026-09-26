class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find lowest buy

        # Find biggest difference
        difference = 0
        buy = prices[0]
        sell = 0
        difference = 0

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif (prices[i] - buy) > difference:
                difference = prices[i] - buy
        
        return difference

        