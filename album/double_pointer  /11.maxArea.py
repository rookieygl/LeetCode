"""
11.盛水最多的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
"""


class Solution(object):
    # 官方 未创建左右指针值的对象，多取了一次
    def maxArea(self, height):
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxArea = max(min(height[left], height[right]) * (right - left), maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


if __name__ == '__main__':
    solution = Solution()
    area = solution.maxArea([4, 3, 2, 1, 4])
    print(area)
