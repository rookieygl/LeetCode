"""
股票最大收益
7天的股票数据，算出最大收益
"""


class Solution(object):
    def maxProfit(self, prices):
        minPrice, profit = 0, 0
        for index in range(len(prices)):
            if index == 0:
                minPrice = prices[index]
            profit = max(profit, prices[index] - minPrice)
            minPrice = min(prices[index], minPrice)
        return profit


if __name__ == '__main__':
    solution = Solution()
    profit = solution.maxProfit([7, 1, 5, 3, 6, 4])
    print(profit)
