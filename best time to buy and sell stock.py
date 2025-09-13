class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        daytoBuy = prices[0]
        profit = 0
        for x in prices: # iterate through prices
            if x < daytoBuy: #check if we found a low price day
                daytoBuy = x # save the low price
            else:
                if x - daytoBuy > profit: # if not low check if we sold; if we make any good profit
                    profit = x - daytoBuy

        return profit # best profit