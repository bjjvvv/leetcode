'''
    Say you have an array for which the ith element is the price of a given 
stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one 
and sell one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # more pythonic version
        return sum([y - x for x, y in zip(prices[:-1], prices[1:]) if x < y])

if __name__ == '__main__':
    prices = [1, 4, 3, 2, 7, 7, 6, 5]
    sol = Solution()
    print(sol.maxProfit(prices))
    prices2 = []
    print(sol.maxProfit(prices2))
