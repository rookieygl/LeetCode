"""
目标和
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
"""


class Solution(object):
    # dfs 深度搜索、回溯 暴力求解 超出时间限制
    def findTargetSumWays_dfs(self, nums, target):
        def dfs(nums, target, u, cur):
            if u == len(nums):
                return 1 if cur == target else 0
            left = dfs(nums, target, u + 1, cur + nums[u])
            right = dfs(nums, target, u + 1, cur - nums[u])
            return left + right

        return dfs(nums, target, 0, 0)

    # 记忆dfs
    def findTargetSumWays_dfsHash(self, nums, target):
        cache = {}

        def dfs(nums, target, u, cur):
            key = str(u) + "_" + str(cur)
            if key in cache:
                return cache[key]
            if u == len(nums):
                cache[key] = 1 if cur == target else 0
                return cache[key]
            left = dfs(nums, target, u + 1, cur + nums[u])
            right = dfs(nums, target, u + 1, cur - nums[u])
            cache[key] = left + right
            return cache[key]

        return dfs(nums, target, 0, 0)

    # 动态求组合
    def findTargetSumWays_dp(self, nums, target):
        sum_n, length = sum(nums), len(nums)  # 求和，数组长度
        if target > sum_n or (sum_n - target) % 2 != 0:  # 边界条件
            return 0
        mid = (sum_n - target) // 2
        dp = [[0 for _ in range(mid + 1)] for _ in range(length + 1)]
        dp[0][0] = 1
        for i in range(1, length + 1):
            x = nums[i - 1]
            for j in range(0, mid + 1):
                dp[i][j] += dp[i - 1][j]
                if j >= x:  # 满足条件
                    dp[i][j] += dp[i - 1][j - x]
        return dp[length][mid]


if __name__ == '__main__':
    solution = Solution()
    fun = solution.findTargetSumWays_dp([1, 1, 1, 1, 1], 3)
    print(fun)
