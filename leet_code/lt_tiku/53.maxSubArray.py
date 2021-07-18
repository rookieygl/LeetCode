"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


class Solution(object):
    def maxSubArray(self, nums):
        pre, maxAns = 0, nums[0]
        for num in nums:
            pre = max(num, num + pre)
            maxAns = max(maxAns, pre)
        return maxAns


if __name__ == '__main__':
    solution = Solution()
    fun = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(fun)
