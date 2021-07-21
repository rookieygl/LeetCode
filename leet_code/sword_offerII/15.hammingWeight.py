"""
剑指 Offer 15. 二进制中1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
"""


class Solution(object):
    # 系统函数
    def hammingWeight_fun(self, n):
        return bin(n).count("1")

    # 循环
    def hammingWeight_loop(self, n):
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans

    # 循环优化
    def hammingWeight_loop(self, n):
        ret = 0
        while n:
            ret += 1
            n &= n - 1
        return ret


if __name__ == '__main__':
    solution = Solution()
    fun = solution.hammingWeight_loop(9)
    print(fun)
