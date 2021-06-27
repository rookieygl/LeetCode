"""
一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
"""


class Solution(object):
    # 三叶 解法
    def findMaxForm(self, strs, m, n):
        length = len(strs)
        cnt = [[0 for _ in range(2)] for _ in range(length)]
        for index, strI in enumerate(strs):  # 计算每个字符串0和1的个数，cnt记录位置和个数
            zero, one = 0, 0
            for c in strI:
                if c == "0":
                    zero += 1
                else:
                    one += 1
            cnt[index] = [zero, one]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 创建dp
        for k in range(length):
            zero, one = cnt[k][0], cnt[k][1]
            for i in range(m, zero - 1, -1):  # 判断字符串是否能放入dp
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)  # 每次元素必然加一，比较较大的元素存入dp
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3)
    print(fun)
