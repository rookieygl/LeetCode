"""
2 的幂
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

数学原理：
2为正数，x为整数，n为整数，那么n必大于0

x为小数时，n为大于0小于1的小数

一个数 n 是 2 的幂，当且仅当 n 是正整数，并且 n 的二进制表示中仅包含 1 个 1
"""


class Solution(object):
    # n 是 2 的幂 最高位为1 其余为0为0
    # n-1 最高位是0 其余位是1 所以 n & (n - 1) == 0
    def isPowerOfTwo_minus(self, n):
        return n > 0 and n & (n - 1) == 0

    # n 是 2 的幂 最高位为1 其余为0为0
    # -n 是n的最高位不变，其余取反 所以 n == n & -n
    def isPowerOfTwo_nverse(self, n):
        return 0 < n == n & -n

    # 2的最大n次幂和任何2的幂取模为0
    def isPowerOfTwo_model(self, n):
        Big = 2 ** 30
        return n > 0 and Big % n == 0

    def bindigits(self, n, bits):
        s = bin(n & int("1" * bits, 2))[2:]
        return ("{0:0>%s}" % (bits)).format(s)


if __name__ == '__main__':
    solution = Solution()
    fun = solution.bindigits(-16, 8)
    print(fun)
