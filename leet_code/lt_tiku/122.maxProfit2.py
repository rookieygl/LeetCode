"""
122. 买卖股票的最佳时机 II
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

贪心算法，每次收益都计算在内
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
