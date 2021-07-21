"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。
"""


class Solution(object):
    #   先填充最小的硬币，依次填入较大硬币，就能减少硬币的个数
    def coinChange(self, amount, coins):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)  # 加入一个硬币记一次数，再取最小值
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    fun = solution.coinChange(amount=5, coins=[1, 2, 5])
    print(fun)
