"""
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
