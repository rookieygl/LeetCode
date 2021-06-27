"""
买卖股票的最佳时机2
无冷却期，可以多次买卖，但是不能重复买入
"""


class Solution(object):
    def maxProfit2(self, prices):
        allProfit = 0
        for index in range(1, len(prices)):
            if prices[index] - prices[index - 1] > 0:
                allProfit += prices[index] - prices[index - 1]
        return allProfit


if __name__ == '__main__':
    solution = Solution()
    profit = solution.maxProfit2([7, 1, 5, 3, 6, 4])
    print(profit)
