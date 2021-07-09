"""
7.整数反转

给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

/ 除 //整数取商 % 整除取余
"""


class Solution(object):
    def reverse(self, x: int) -> int:
        num_max, num_min = 2 ** 31 - 1, -2 ** 31
        re_num = 0
        while x != 0:
            # num_min 也是一个负数，不能写成 rev < INT_MIN // 10
            if re_num > num_max / 10 or re_num < num_min / 10 + 1:
                return 0
            digit = x % 10
            # 处理负数取模 字符串转换整数 (atoi)
            # 取模运算在 x 为负数时也会返回 [0, 9) 例 -1 % 10 =9 1 % 10 =1
            # 同时整除时无需取反，否则会导致digit由0变成10
            if x < 0 and digit > 0:
                # 取反
                digit -= 10
            # 整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            # 减去（负数是加上）余数，将x保持为10的整倍数，防止x变小
            # 例如 -11//10 是-2 -10//10才是1, 除法无此限制
            x = (x - digit) // 10
            re_num = 10 * re_num + digit
        return int(re_num)


if __name__ == '__main__':
    solution = Solution()
    reverse = solution.reverse(-19)
    print(reverse)
