"""
4的幂

给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false。
整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x
"""


class Solution(object):

    def isPowerOfFour_minus(self, n):
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0

    # 如果 n 是 4的幂，那么它可以表示成 4^x的形式，我们可以发现它除以 3 的余数一定为 1
    def isPowerOfFour_model(self, n):
        big = 2 ** 30
        return n > 0 and n % 3 == 1 and big % n == 0


if __name__ == '__main__':
    solution = Solution()
    fun = solution.isPowerOfFour_model(7)
    print(fun)
