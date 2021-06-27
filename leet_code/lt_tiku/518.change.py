"""
518. 零钱兑换 II

给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
假设每一种面额的硬币有无限个。 
题目数据保证结果符合 32 位带符号整数。
"""


class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.change(amount=5, coins=[1, 2, 5])
    print(fun)
