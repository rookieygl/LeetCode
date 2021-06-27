"""
你能在你最喜欢的那天吃到你最喜欢的糖果吗？

给你一个下标从 0 开始的正整数数组 candiesCount ，其中 candiesCount[i] 表示你拥有的第 i 类糖果的数目。
同时给你一个二维数组 queries ，其中 queries[i] = [favoriteTypei, favoriteDayi, dailyCapi] 。

你按照如下规则进行一场游戏：

你从第 0 天开始吃糖果。
你在吃完 所有 第 i - 1 类糖果之前，不能 吃任何一颗第 i 类糖果。
在吃完所有糖果之前，你必须每天 至少 吃 一颗 糖果。
请你构建一个布尔型数组 answer ，满足 answer.length == queries.length 。answer[i] 为 true 的条件是：
在每天吃不超过 dailyCapi 颗糖果的前提下，你可以在第 favoriteDayi 天吃到第 favoriteTypei 类糖果；否则 answer[i] 为 false 。
注意，只要满足上面 3 条规则中的第二条规则，你就可以在同一天吃不同类型的糖果。

请你返回得到的数组 answer 。
"""
from itertools import accumulate

class Solution(object):
    def canEat(self, candiesCount, queries):
        # 前缀和
        total = list(accumulate(candiesCount))
        ans = list()
        for favoriteType, favoriteDay, dailyCap in queries:
            x1 = favoriteDay + 1
            y1 = x1 * dailyCap
            x2 = 1 if favoriteType == 0 else total[favoriteType - 1] + 1
            y2 = total[favoriteType]

            ans.append(not(x1 > y2 or y1 < x2))
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.canEat(candiesCount=[7, 4, 5, 3, 8], queries=[[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]])
    print(fun)
