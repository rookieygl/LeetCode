"""
最后一块石头的重量 II
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

"""


class Solution(object):
    # 三叶
    def lastStoneWeightII_three(self, stones):
        length, total = len(stones), sum(stones)
        mid = total // 2
        dp = [0] * (mid + 1)  # [0 for _ in range(length + 1)]
        for i in range(1, length + 1):
            x = stones[i - 1]
            for j in range(mid, x - 1, -1):
                dp[j] = max(dp[j], dp[j - x] + x)
        return total - dp[mid] - dp[mid]

    #  lt官方 更快一点
    def lastStoneWeightII_lt(self, stones):
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [False] * (m + 1)
        dp[0] = True
        for weight in stones:
            for j in range(m, weight - 1, -1):
                dp[j] |= dp[j - weight]
        ans = None
        for j in range(m, -1, -1):
            if dp[j]:
                ans = total - 2 * j
                break
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.lastStoneWeightII_three([2, 7, 4, 1, 8, 1])
    print(fun)
