"""
完全平方数

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
"""


class Solution(object):
    # 三叶
    def numSquares_three(self, n):
        MAX_VALUE = 2 ** 31 - 1
        dp = [MAX_VALUE] * (n + 1)
        dp[0] = 0
        t = 1
        while n >= t ** 2:
            x = t ** 2
            j = x
            while n >= j:
                dp[j] = min(dp[j], dp[j - x] + 1)
                j += 1

            t += 1
        return dp[n]

    # 比较边界 超时
    def numSquares_compare(self, n):
        dp = [0] * (n + 1)  # 默认初始化值都为0
        for i in range(1, n + 1):
            dp[i] = i  # 最坏的情况就是每次+1
            j = 1
            while i >= j ** 2:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[n]

    # 超时
    def numSquares_lt(self, n):
        dp = [0] * (n + 1)
        MAX_VALUE = 2 ** 31 - 1
        for i in range(1, n + 1):
            minn = MAX_VALUE
            j = 1
            while i >= j ** 2:
                minn = min(minn, dp[i - j ** 2])
                j += 1
            dp[i] = minn + 1
        return dp[n]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.numSquares_three(12)
    print(fun)
