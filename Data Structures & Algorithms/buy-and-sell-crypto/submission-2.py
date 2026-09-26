class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find lowest buy

        # Find biggest difference
        buy = prices[0]
        difference = 0

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                difference = max(difference, prices[i] - buy)
        
        return difference

        