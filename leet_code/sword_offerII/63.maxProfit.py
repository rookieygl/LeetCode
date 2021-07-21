"""
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
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
