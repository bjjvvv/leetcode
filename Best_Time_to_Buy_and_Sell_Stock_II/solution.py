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

        # 这个判断和 if not prices: 一样，有点纠结用哪一种
        if prices is None or len(prices) == 0:
            return 0

        previous_price = prices[0]
        profit = 0
        for p in prices[1: ]:
            if previous_price < p:
                profit += p - previous_price
            previous_price = p
        
        return profit

if __name__ == '__main__':
    prices = [1, 4, 3, 2, 7, 7, 6, 5]
    sol = Solution()
    print(sol.maxProfit(prices))
    prices2 = []
    prices3 = None
    print(sol.maxProfit(prices2), sol.maxProfit(prices3) )
