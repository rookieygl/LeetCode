"""
        length = len(piles)
        dp = [0] * length
        for i, pile in enumerate(piles):
            dp[i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[length - 1] > 0
"""


class Solution(object):
    # 官方dp
    def stoneGame_lt_dp(self, piles):
        length = len(piles)
        dp = [pile for pile in piles]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[length - 1] > 0

    # 尝试双指针
    def stoneGame_lt_double(self, piles):
        count, start, end = 0, 0, len(piles) - 1
        while start < end:
            count += max(piles[start], piles[end]) - min(piles[start], piles[end])
            start += 1
            end -= 1
        return count > 0


if __name__ == '__main__':
    solution = Solution()
    fun = solution.stoneGame_lt_double([5, 3, 4, 5])
    print(fun)
