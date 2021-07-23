"""
1893. 检查是否区域内所有整数都被覆盖
1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50

for l, r in ranges: 遍历二维数组的两列
"""


class Solution(object):
    def isCovered(self, ranges, left, right):
        diff = [0] * 52  # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    fun = solution.isCovered([[1, 2], [3, 4], [6, 6]], left=2, right=5)
    print(fun)
