"""
58广告算法 三轮

算法题
1、二叉树的非递归遍历(中序即可)
2、两个链表是否相交
3、最长公共子序列
"""


class Solution(object):
    # 最长公共子序列 字符串顺序不变 动态规划
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.longestCommonSubsequence("eaca", "ddaac")
    print(fun)
