"""
剑指 Offer 10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""


class Solution(object):
    # 递归 栈深度两边一样，不是最优解
    def fib_recursion(self, n):
        if n < 2:
            return n
        fib = self.fib_recursion(n - 1) + self.fib_recursion(n - 2)
        return fib % 1000000007

    # 动态记忆上个斐波那契的值
    def fib_dp(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    solution = Solution()
    fun = solution.fib_recursion(3)
    print(fun)
