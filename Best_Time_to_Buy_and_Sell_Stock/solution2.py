'''
    Say you have an array for which the ith element is the price of a given 
stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one 
and sell one share of the stock), design an algorithm to find the maximum profit.
'''

# more concise but slower
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 1:
            return 0

        cur_min_price = prices[0]
        profit = 0
        for p in prices[1: ]:
            profit = max(p - cur_min_price, profit)
            cur_min_price = min(p, cur_min_price)
                
        return profit


if __name__ == '__main__':
    prices = [1, 4, 3, 2, 7, 7, 6, 5]
    sol = Solution()
    print(sol.maxProfit(prices))
    prices2 = []
    prices3 = None
    print(sol.maxProfit(prices2), sol.maxProfit(prices3) )
