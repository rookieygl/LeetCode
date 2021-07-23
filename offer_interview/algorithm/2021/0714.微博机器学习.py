"""
二面
1. 等式组合
求出a3+b3 = c3+d3所有组合
abcd取值范围1-1000
三面
1. 字符串组合
2. 不同路径 LC62
"""
import collections
import math


class Solution(object):
    def combination(self):
        pow_map = collections.defaultdict(list)
        pow_repeat = collections.defaultdict(str)
        for a in range(1, 10):
            for b in range(1, 10):
                pow_sum = math.pow(a, 3) + math.pow(b, 3)
                comb = "%d+%d" % (a, b)
                comb = str(comb)
                if comb in pow_repeat:
                    continue
                pow_repeat[comb] = True
                pow_map[pow_sum].append(comb)

        def dfs(comb_list, result_list):
            print(str(key) + ":" + str(comb_list))
            if len(comb_list) == 0:
                result_list.append("=".join(path))
                return
            for i in range(len(comb_list)):
                path.append(comb_list[i])
                dfs(comb_list[:i] + comb_list[i + 1:], result_list)
                path.pop()
            return result_list

        for key, value_list in pow_map.items():
            path = []
            result_list = []
            if len(value_list) <= 1:
                result_list.append("%s=%s" % (value_list[0], value_list[0]))
            else:
                result_list = dfs(value_list, result_list)
            print(result_list)
        return

    def combination_str(self, str):
        return str

    def uniquePaths(self, m, n):
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    combination_str = solution.combination_str("aaccc")
    print(combination_str)
    combination_str = solution.uniquePaths(3, 7)
    print(combination_str)
