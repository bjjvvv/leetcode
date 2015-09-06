'''
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0

        max_profit_forward = [0] * l
        max_profit_backward = [0] * l
        
        cur_min_fw = prices[0]
        cur_max_bw = prices[-1]
        for i in range(1, l):
            max_profit_forward[i] = max(max_profit_forward[i-1],
                                        prices[i] - cur_min_fw)
            max_profit_backward[-i-1] = max(max_profit_backward[-i],
                                        cur_max_bw - prices[-i-1])
            cur_min_fw = min(prices[i], cur_min_fw)
            cur_max_bw = max(prices[-i-1], cur_max_bw)

        return max(x + y for x, y in zip([0] + max_profit_forward,
                                        max_profit_backward + [0]))

if __name__ == '__main__':
    prices = [1,2,3,1,2,3]
    sol = Solution()
    max_profit = sol.maxProfit(prices)
    print(max_profit)


            
