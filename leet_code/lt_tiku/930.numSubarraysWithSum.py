"""
930. 和相同的二元子数组
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。
"""
from collections import defaultdict


class Solution(object):
    #  hash+前缀和
    def numSubarraysWithSum(self, nums, goal):
        sumSet = defaultdict(int)
        numSum = 0
        ans = 0
        for i, num in enumerate(nums):
            sumSet[numSum] = sumSet[numSum] + 1  # hash记录前缀和，重复的加1
            numSum += num
            ans += sumSet[numSum - goal]  # 前缀和存在goal时，累加即可
        return ans


if __name__ == '__main__':
    solution = Solution()
    fun = solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2)
    print(fun)
