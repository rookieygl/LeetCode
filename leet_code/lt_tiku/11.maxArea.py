"""
盛水最多的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
"""


class Solution(object):
    # 官方 未创建左右指针值的对象，多取了一次
    def maxArea(self, height):
        leftPo, rightPo = 0, len(height) - 1
        leftVo, rightVo = height[leftPo], height[rightPo]
        area = 0
        while leftPo <= rightPo - 1:
            area = max(min(leftVo, rightVo) * (rightPo - leftPo), area)
            if leftVo > rightVo:
                rightPo -= 1
                rightVo = height[rightPo]
            else:
                leftPo += 1
                leftVo = height[leftPo]
        return area


if __name__ == '__main__':
    solution = Solution()
    area = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(area)
