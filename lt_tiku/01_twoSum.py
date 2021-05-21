"""
两数之和
"""


# -*- coding: utf-8 -*-

# 数组元素可重复
class Solution(object):
    def twoSum(self, nums, target):
        hashtable = dict()
        # 遍历数组和坐标
        for i, num in enumerate(nums):
            # 当差值存在map时，返回坐标即可
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        # 答案不存在的情况
        return []


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 3]
    solution_two_sum = solution.twoSum(nums, 6)
    print(solution_two_sum)
